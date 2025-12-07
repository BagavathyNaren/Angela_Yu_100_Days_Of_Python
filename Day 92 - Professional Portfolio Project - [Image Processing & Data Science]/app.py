from flask import Flask, render_template_string, request, jsonify
import numpy as np
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Image Color Analyzer</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            max-width: 800px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            color: #333;
            margin-bottom: 30px;
            text-align: center;
        }
        .upload-area {
            border: 3px dashed #667eea;
            border-radius: 10px;
            padding: 40px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 30px;
        }
        .upload-area:hover {
            border-color: #764ba2;
            background: #f8f9ff;
        }
        .upload-area.dragover {
            background: #f0f0ff;
            border-color: #764ba2;
        }
        input[type="file"] { display: none; }
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: transform 0.2s;
        }
        .btn:hover { transform: translateY(-2px); }
        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        .preview {
            margin: 20px 0;
            text-align: center;
        }
        .preview img {
            max-width: 100%;
            max-height: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .results {
            margin-top: 30px;
        }
        .color-item {
            display: flex;
            align-items: center;
            padding: 15px;
            margin-bottom: 10px;
            background: #f8f9fa;
            border-radius: 10px;
            transition: transform 0.2s;
        }
        .color-item:hover {
            transform: translateX(5px);
        }
        .color-box {
            width: 60px;
            height: 60px;
            border-radius: 8px;
            margin-right: 20px;
            border: 2px solid #ddd;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .color-info {
            flex: 1;
        }
        .color-hex {
            font-weight: 600;
            font-size: 18px;
            color: #333;
        }
        .color-rgb {
            color: #666;
            font-size: 14px;
            margin-top: 5px;
        }
        .color-percent {
            font-size: 24px;
            font-weight: 700;
            color: #667eea;
        }
        .loading {
            text-align: center;
            padding: 20px;
            color: #667eea;
            font-size: 18px;
        }
        .error {
            background: #fee;
            color: #c33;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 Image Color Analyzer</h1>
        
        <div class="upload-area" id="uploadArea">
            <p style="font-size: 48px; margin-bottom: 10px;">📤</p>
            <p style="font-size: 18px; color: #667eea; font-weight: 600;">
                Click to upload or drag & drop an image
            </p>
            <p style="color: #999; margin-top: 10px;">PNG, JPG, JPEG up to 10MB</p>
            <input type="file" id="fileInput" accept="image/*">
        </div>

        <div class="preview" id="preview"></div>
        <div id="loading" class="loading" style="display:none;">
            Analyzing colors...
        </div>
        <div id="error" class="error" style="display:none;"></div>
        <div id="results" class="results"></div>
    </div>

    <script>
        const uploadArea = document.getElementById('uploadArea');
        const fileInput = document.getElementById('fileInput');
        const preview = document.getElementById('preview');
        const loading = document.getElementById('loading');
        const error = document.getElementById('error');
        const results = document.getElementById('results');

        uploadArea.addEventListener('click', () => fileInput.click());

        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });

        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });

        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            const file = e.dataTransfer.files[0];
            if (file && file.type.startsWith('image/')) {
                handleFile(file);
            }
        });

        fileInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) handleFile(file);
        });

        function handleFile(file) {
            error.style.display = 'none';
            results.innerHTML = '';
            
            const reader = new FileReader();
            reader.onload = (e) => {
                preview.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
                analyzeImage(file);
            };
            reader.readAsDataURL(file);
        }

        function analyzeImage(file) {
            loading.style.display = 'block';
            const formData = new FormData();
            formData.append('image', file);

            fetch('/analyze', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                loading.style.display = 'none';
                if (data.error) {
                    error.textContent = data.error;
                    error.style.display = 'block';
                } else {
                    displayResults(data.colors);
                }
            })
            .catch(err => {
                loading.style.display = 'none';
                error.textContent = 'Error analyzing image: ' + err.message;
                error.style.display = 'block';
            });
        }

        function displayResults(colors) {
            results.innerHTML = '<h2 style="margin-bottom: 20px; color: #333;">Top 10 Colors</h2>';
            colors.forEach((color, idx) => {
                const div = document.createElement('div');
                div.className = 'color-item';
                div.innerHTML = `
                    <div class="color-box" style="background-color: ${color.hex}"></div>
                    <div class="color-info">
                        <div class="color-hex">${color.hex.toUpperCase()}</div>
                        <div class="color-rgb">RGB(${color.rgb[0]}, ${color.rgb[1]}, ${color.rgb[2]})</div>
                    </div>
                    <div class="color-percent">${color.percentage.toFixed(2)}%</div>
                `;
                results.appendChild(div);
            });
        }
    </script>
</body>
</html>
'''

def analyze_image_colors(image_bytes):
    """Extract top 10 most common colors from image using NumPy"""
    # Open image and convert to RGB
    img = Image.open(BytesIO(image_bytes))
    img = img.convert('RGB')
    
    # Resize for performance - no need to analyze every pixel
    img.thumbnail((300, 300))
    
    # Convert to NumPy array
    img_array = np.array(img)
    
    # Reshape to 2D array: (num_pixels, 3)
    pixels = img_array.reshape(-1, 3)
    
    # Quantize colors to reduce similar colors (group into buckets)
    quantize_level = 8
    quantized = (pixels // quantize_level) * quantize_level
    
    # Get unique colors and their counts
    unique_colors, counts = np.unique(quantized, axis=0, return_counts=True)
    
    # Sort by count (descending)
    sorted_indices = np.argsort(counts)[::-1]
    top_colors = unique_colors[sorted_indices][:10]
    top_counts = counts[sorted_indices][:10]
    
    # Calculate percentages
    total_pixels = len(pixels)
    percentages = (top_counts / total_pixels) * 100
    
    # Format results
    results = []
    for color, percentage in zip(top_colors, percentages):
        r, g, b = map(int, color)
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        results.append({
            'rgb': [r, g, b],
            'hex': hex_color,
            'percentage': float(percentage)
        })
    
    return results

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read image bytes
        image_bytes = file.read()
        
        # Analyze colors
        colors = analyze_image_colors(image_bytes)
        
        return jsonify({'colors': colors})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)