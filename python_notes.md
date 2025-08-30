ft Corporation. All rights reserved.

C:\Continuous Learning\100 Days of Code The Complete Python Pro Bootcamp>"C:/Continuous Learning/100 Days of Code The Complete Python Pro Bootcamp/.venv/Scripts/activate.bat"

(.venv) C:\Continuous Learning\100 Days of Code The Complete Python Pro Bootcamp>"C:/Continuous Learning/100 Days of Code The Complete Python Pro Bootcamp/.venv/Scripts/python.exe" "c:/Continuous Learning/100 Days of Code The Complete Python Pro Bootcamp/Day-40-FlightSearchAmadeus/main.py"
{'prices': [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
            {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42}, 
            {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},    
            {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
            {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
            {'city': 'Kuala Lumpur',
             'iataCode': '',
             'id': 7,
             'lowestPrice': 414},
            {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
            {'city': 'San Francisco',
             'iataCode': '',
             'id': 9,
             'lowestPrice': 260},
            {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]}
Your token is qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Your token expires in 1799 seconds
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 2,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=Paris&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Paris",
    "iataCode" : "PAR",
    "address" : {
      "countryCode" : "FR",
      "stateCode" : "FR-75"
    },
    "geoCode" : {
      "latitude" : 48.85341,
      "longitude" : 2.3488
    },
    "relationships" : [ {
      "id" : "BVA",
      "type" : "Airport",
      "href" : "#/included/airports/BVA"
    }, {
      "id" : "CDG",
      "type" : "Airport",
      "href" : "#/included/airports/CDG"
    }, {
      "id" : "ORY",
      "type" : "Airport",
      "href" : "#/included/airports/ORY"
    }, {
      "id" : "XCR",
      "type" : "Airport",
      "href" : "#/included/airports/XCR"
    } ]
  }, {
    "type" : "location",
    "subType" : "city",
    "name" : "Le Touquet-Paris-Plage",
    "iataCode" : "LTQ",
    "address" : {
      "countryCode" : "FR",
      "stateCode" : "FR-62"
    },
    "geoCode" : {
      "latitude" : 50.52432,
      "longitude" : 1.58571
    },
    "relationships" : [ {
      "id" : "LIL",
      "type" : "Airport",
      "href" : "#/included/airports/LIL"
    } ]
  } ],
  "included" : {
    "airports" : {
      "XCR" : {
        "subType" : "Airport",
        "name" : "Chalons-Vatry",
        "iataCode" : "XCR",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 48.77611,
          "longitude" : 4.18444
        }
      },
      "CDG" : {
        "subType" : "Airport",
        "name" : "Charles de Gaulle",
        "iataCode" : "CDG",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 49.01278,
          "longitude" : 2.55
        }
      },
      "ORY" : {
        "subType" : "Airport",
        "name" : "Orly",
        "iataCode" : "ORY",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 48.72528,
          "longitude" : 2.35944
        }
      },
      "BVA" : {
        "subType" : "Airport",
        "name" : "Beauvais-Tille",
        "iataCode" : "BVA",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 49.45444,
          "longitude" : 2.11278
        }
      },
      "LIL" : {
        "subType" : "Airport",
        "name" : "Lesquin",
        "iataCode" : "LIL",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-59"
        },
        "geoCode" : {
          "latitude" : 50.57037,
          "longitude" : 3.10643
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 2,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=Frankfurt&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Frankfurt am Main",
    "iataCode" : "FRA",
    "address" : {
      "countryCode" : "DE",
      "stateCode" : "DE-ZZZ"
    },
    "geoCode" : {
      "latitude" : 50.11552,
      "longitude" : 8.68417
    },
    "relationships" : [ {
      "id" : "FRA",
      "type" : "Airport",
      "href" : "#/included/airports/FRA"
    }, {
      "id" : "HHN",
      "type" : "Airport",
      "href" : "#/included/airports/HHN"
    } ]
  }, {
    "type" : "location",
    "subType" : "city",
    "name" : "Frankfurt (Oder)",
    "iataCode" : "ZFR",
    "address" : {
      "countryCode" : "DE",
      "stateCode" : "DE-ZZZ"
    },
    "geoCode" : {
      "latitude" : 52.34714,
      "longitude" : 14.55062
    },
    "relationships" : [ {
      "id" : "BER",
      "type" : "Airport",
      "href" : "#/included/airports/BER"
    }, {
      "id" : "SXF",
      "type" : "Airport",
      "href" : "#/included/airports/SXF"
    }, {
      "id" : "TXL",
      "type" : "Airport",
      "href" : "#/included/airports/TXL"
    } ]
  } ],
  "included" : {
    "airports" : {
      "SXF" : {
        "subType" : "Airport",
        "name" : "Schoenefeld",
        "iataCode" : "SXF",
        "address" : {
          "countryCode" : "DE",
          "stateCode" : "DE-ZZZ"
        },
        "geoCode" : {
          "latitude" : 52.38,
          "longitude" : 13.5225
        }
      },
      "FRA" : {
        "subType" : "Airport",
        "name" : "International",
        "iataCode" : "FRA",
        "address" : {
          "countryCode" : "DE",
          "stateCode" : "DE-ZZZ"
        },
        "geoCode" : {
          "latitude" : 50.0406,
          "longitude" : 8.55603
        }
      },
      "TXL" : {
        "subType" : "Airport",
        "name" : "Tegel",
        "iataCode" : "TXL",
        "address" : {
          "countryCode" : "DE",
          "stateCode" : "DE-ZZZ"
        },
        "geoCode" : {
          "latitude" : 52.55969,
          "longitude" : 13.28771
        }
      },
      "BER" : {
        "subType" : "Airport",
        "name" : "Brandenburg",
        "iataCode" : "BER",
        "address" : {
          "countryCode" : "DE",
          "stateCode" : "DE-ZZZ"
        },
        "geoCode" : {
          "latitude" : 52.36213,
          "longitude" : 13.50168
        }
      },
      "HHN" : {
        "subType" : "Airport",
        "name" : "Hahn",
        "iataCode" : "HHN",
        "address" : {
          "countryCode" : "DE",
          "stateCode" : "DE-ZZZ"
        },
        "geoCode" : {
          "latitude" : 49.948673,
          "longitude" : 7.263892
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 2,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=Tokyo&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Tokyo",
    "iataCode" : "TYO",
    "address" : {
      "countryCode" : "JP",
      "stateCode" : "JP-ZZZ"
    },
    "geoCode" : {
      "latitude" : 35.6895,
      "longitude" : 139.69171
    },
    "relationships" : [ {
      "id" : "HND",
      "type" : "Airport",
      "href" : "#/included/airports/HND"
    }, {
      "id" : "NRT",
      "type" : "Airport",
      "href" : "#/included/airports/NRT"
    } ]
  }, {
    "type" : "location",
    "subType" : "city",
    "name" : "Nishi-Tokyo-shi",
    "address" : {
      "countryCode" : "JP",
      "stateCode" : "JP-ZZZ"
    },
    "geoCode" : {
      "latitude" : 35.72526,
      "longitude" : 139.5383
    },
    "relationships" : [ {
      "id" : "HND",
      "type" : "Airport",
      "href" : "#/included/airports/HND"
    }, {
      "id" : "NRT",
      "type" : "Airport",
      "href" : "#/included/airports/NRT"
    } ]
  } ],
  "included" : {
    "airports" : {
      "NRT" : {
        "subType" : "Airport",
        "name" : "Narita Intl",
        "iataCode" : "NRT",
        "address" : {
          "countryCode" : "JP",
          "stateCode" : "JP-ZZZ"
        },
        "geoCode" : {
          "latitude" : 35.76472,
          "longitude" : 140.38638
        }
      },
      "HND" : {
        "subType" : "Airport",
        "name" : "Tokyo Intl (Haneda)",
        "iataCode" : "HND",
        "address" : {
          "countryCode" : "JP",
          "stateCode" : "JP-ZZZ"
        },
        "geoCode" : {
          "latitude" : 35.552258,
          "longitude" : 139.7797
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 1,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=Hong+Kong&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Hong Kong",
    "iataCode" : "HKG",
    "address" : {
      "countryCode" : "HK",
      "stateCode" : "HK-ZZZ"
    },
    "geoCode" : {
      "latitude" : 22.27832,
      "longitude" : 114.17469
    },
    "relationships" : [ {
      "id" : "HKG",
      "type" : "Airport",
      "href" : "#/included/airports/HKG"
    } ]
  } ],
  "included" : {
    "airports" : {
      "HKG" : {
        "subType" : "Airport",
        "name" : "International",
        "iataCode" : "HKG",
        "address" : {
          "countryCode" : "HK",
          "stateCode" : "HK-ZZZ"
        },
        "geoCode" : {
          "latitude" : 22.31459,
          "longitude" : 113.93243
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 1,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=Istanbul&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Istanbul",
    "iataCode" : "IST",
    "address" : {
      "countryCode" : "TR",
      "stateCode" : "TR-ZZZ"
    },
    "geoCode" : {
      "latitude" : 41.01384,
      "longitude" : 28.94966
    },
    "relationships" : [ {
      "id" : "IST",
      "type" : "Airport",
      "href" : "#/included/airports/IST"
    }, {
      "id" : "SAW",
      "type" : "Airport",
      "href" : "#/included/airports/SAW"
    } ]
  } ],
  "included" : {
    "airports" : {
      "SAW" : {
        "subType" : "Airport",
        "name" : "Sabiha Gokcen",
        "iataCode" : "SAW",
        "address" : {
          "countryCode" : "TR",
          "stateCode" : "TR-ZZZ"
        },
        "geoCode" : {
          "latitude" : 40.89861,
          "longitude" : 29.30917
        }
      },
      "IST" : {
        "subType" : "Airport",
        "name" : "Istanbul Airport",
        "iataCode" : "IST",
        "address" : {
          "countryCode" : "TR",
          "stateCode" : "TR-ZZZ"
        },
        "geoCode" : {
          "latitude" : 41.2629,
          "longitude" : 28.74242
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 1,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=Kuala+Lumpur&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Kuala Lumpur",
    "iataCode" : "KUL",
    "address" : {
      "countryCode" : "MY",
      "stateCode" : "MY-ZZZ"
    },
    "geoCode" : {
      "latitude" : 3.1412,
      "longitude" : 101.68653
    },
    "relationships" : [ {
      "id" : "KUL",
      "type" : "Airport",
      "href" : "#/included/airports/KUL"
    }, {
      "id" : "SZB",
      "type" : "Airport",
      "href" : "#/included/airports/SZB"
    } ]
  } ],
  "included" : {
    "airports" : {
      "KUL" : {
        "subType" : "Airport",
        "name" : "International",
        "iataCode" : "KUL",
        "address" : {
          "countryCode" : "MY",
          "stateCode" : "MY-ZZZ"
        },
        "geoCode" : {
          "latitude" : 2.74558,
          "longitude" : 101.70992
        }
      },
      "SZB" : {
        "subType" : "Airport",
        "name" : "Sultan Abdul Aziz Shah",
        "iataCode" : "SZB",
        "address" : {
          "countryCode" : "MY",
          "stateCode" : "MY-ZZZ"
        },
        "geoCode" : {
          "latitude" : 3.130583,
          "longitude" : 101.54933
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 2,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=New+York&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "New York City",
    "iataCode" : "NYC",
    "address" : {
      "countryCode" : "US",
      "stateCode" : "US-NY"
    },
    "geoCode" : {
      "latitude" : 40.71427,
      "longitude" : -74.00597
    },
    "relationships" : [ {
      "id" : "EWR",
      "type" : "Airport",
      "href" : "#/included/airports/EWR"
    }, {
      "id" : "JFK",
      "type" : "Airport",
      "href" : "#/included/airports/JFK"
    }, {
      "id" : "LGA",
      "type" : "Airport",
      "href" : "#/included/airports/LGA"
    }, {
      "id" : "NYS",
      "type" : "Airport",
      "href" : "#/included/airports/NYS"
    }, {
      "id" : "SWF",
      "type" : "Airport",
      "href" : "#/included/airports/SWF"
    } ]
  }, {
    "type" : "location",
    "subType" : "city",
    "name" : "East New York",
    "address" : {
      "countryCode" : "US",
      "stateCode" : "US-NY"
    },
    "geoCode" : {
      "latitude" : 40.66677,
      "longitude" : -73.88236
    },
    "relationships" : [ {
      "id" : "EWR",
      "type" : "Airport",
      "href" : "#/included/airports/EWR"
    }, {
      "id" : "JFK",
      "type" : "Airport",
      "href" : "#/included/airports/JFK"
    }, {
      "id" : "LGA",
      "type" : "Airport",
      "href" : "#/included/airports/LGA"
    }, {
      "id" : "NYS",
      "type" : "Airport",
      "href" : "#/included/airports/NYS"
    }, {
      "id" : "SWF",
      "type" : "Airport",
      "href" : "#/included/airports/SWF"
    } ]
  } ],
  "included" : {
    "airports" : {
      "EWR" : {
        "subType" : "Airport",
        "name" : "Newark Liberty Intl",
        "iataCode" : "EWR",
        "address" : {
          "countryCode" : "US",
          "stateCode" : "US-NY"
        },
        "geoCode" : {
          "latitude" : 40.69125,
          "longitude" : -74.17883
        }
      },
      "SWF" : {
        "subType" : "Airport",
        "name" : "Stewart International",
        "iataCode" : "SWF",
        "address" : {
          "countryCode" : "US",
          "stateCode" : "US-NY"
        },
        "geoCode" : {
          "latitude" : 41.49874,
          "longitude" : -74.10045
        }
      },
      "LGA" : {
        "subType" : "Airport",
        "name" : "LaGuardia",
        "iataCode" : "LGA",
        "address" : {
          "countryCode" : "US",
          "stateCode" : "US-NY"
        },
        "geoCode" : {
          "latitude" : 40.77607,
          "longitude" : -73.87269
        }
      },
      "NYS" : {
        "subType" : "Airport",
        "name" : "Skyports SPB",
        "iataCode" : "NYS",
        "address" : {
          "countryCode" : "US",
          "stateCode" : "US-NY"
        },
        "geoCode" : {
          "latitude" : 40.73513,
          "longitude" : -73.9729
        }
      },
      "JFK" : {
        "subType" : "Airport",
        "name" : "John F Kennedy Intl",
        "iataCode" : "JFK",
        "address" : {
          "countryCode" : "US",
          "stateCode" : "US-NY"
        },
        "geoCode" : {
          "latitude" : 40.63983,
          "longitude" : -73.77874
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 2,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=San+Francisco&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "San Francisco",
    "iataCode" : "SFO",
    "address" : {
      "countryCode" : "US",
      "stateCode" : "US-CA"
    },
    "geoCode" : {
      "latitude" : 37.77493,
      "longitude" : -122.41942
    },
    "relationships" : [ {
      "id" : "SFO",
      "type" : "Airport",
      "href" : "#/included/airports/SFO"
    } ]
  }, {
    "type" : "location",
    "subType" : "city",
    "name" : "San Francisco",
    "address" : {
      "countryCode" : "AR",
      "stateCode" : "AR-X"
    },
    "geoCode" : {
      "latitude" : -31.42797,
      "longitude" : -62.08266
    },
    "relationships" : [ {
      "id" : "COR",
      "type" : "Airport",
      "href" : "#/included/airports/COR"
    } ]
  } ],
  "included" : {
    "airports" : {
      "COR" : {
        "subType" : "Airport",
        "name" : "A.L.V. Taravella",
        "iataCode" : "COR",
        "address" : {
          "countryCode" : "AR",
          "stateCode" : "AR-X"
        },
        "geoCode" : {
          "latitude" : -31.32362,
          "longitude" : -64.20795
        }
      },
      "SFO" : {
        "subType" : "Airport",
        "name" : "International",
        "iataCode" : "SFO",
        "address" : {
          "countryCode" : "US",
          "stateCode" : "US-CA"
        },
        "geoCode" : {
          "latitude" : 37.618973,
          "longitude" : -122.374886
        }
      }
    }
  }
}
Using this token to get destination qM9SLqzD8QEf1fw6SEhgnkyCDPjC
Status code 200. Airport IATA: {
  "meta" : {
    "count" : 2,
    "links" : {
      "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=Dublin&max=2"
    }
  },
  "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Dublin",
    "iataCode" : "DBN",
    "address" : {
      "countryCode" : "US",
      "stateCode" : "US-GA"
    },
    "geoCode" : {
      "latitude" : 32.54044,
      "longitude" : -82.90375
    },
    "relationships" : [ {
      "id" : "DBN",
      "type" : "Airport",
      "href" : "#/included/airports/DBN"
    } ]
  }, {
    "type" : "location",
    "subType" : "city",
    "name" : "Dublin",
    "iataCode" : "DUB",
    "address" : {
      "countryCode" : "IE",
      "stateCode" : "IE-ZZZ"
    },
    "geoCode" : {
      "latitude" : 53.33306,
      "longitude" : -6.24889
    },
    "relationships" : [ {
      "id" : "DUB",
      "type" : "Airport",
      "href" : "#/included/airports/DUB"
    } ]
  } ],
  "included" : {
    "airports" : {
      "DUB" : {
        "subType" : "Airport",
        "name" : "International",
        "iataCode" : "DUB",
        "address" : {
          "countryCode" : "IE",
          "stateCode" : "IE-ZZZ"
        },
        "geoCode" : {
          "latitude" : 53.42133,
          "longitude" : -6.27008
        }
      },
      "DBN" : {
        "subType" : "Airport",
        "name" : "W.H. \"Bud\" Barron",
        "iataCode" : "DBN",
        "address" : {
          "countryCode" : "US",
          "stateCode" : "US-GA"
        },
        "geoCode" : {
          "latitude" : 32.56406,
          "longitude" : -82.98653
        }
      }
    }
  }
}
sheet_data:
 [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}]
{
  "price": {
    "iataCode": "PAR",
    "id": 2
  }
}
{
  "price": {
    "iataCode": "FRA",
    "id": 3
  }
}
{
  "price": {
    "iataCode": "TYO",
    "id": 4
  }
}
{
  "price": {
    "iataCode": "HKG",
    "id": 5
  }
}
{
  "price": {
    "iataCode": "IST",
    "id": 6
  }
}
{
  "price": {
    "iataCode": "KUL",
    "id": 7
  }
}
{
  "price": {
    "iataCode": "NYC",
    "id": 8
  }
}
{
  "price": {
    "iataCode": "SFO",
    "id": 9
  }
}
{
  "price": {
    "iataCode": "DBN",
    "id": 10
  }
}
Getting direct flights for Paris...
Paris: £197.22
Getting direct flights for Frankfurt...
Frankfurt: £290.26
Getting direct flights for Tokyo...
Tokyo: £1117.42
Getting direct flights for Hong Kong...
Hong Kong: £1358.22
Getting direct flights for Istanbul...
Istanbul: £318.28
Getting direct flights for Kuala Lumpur...
Kuala Lumpur: £982.42
Getting direct flights for New York...
New York: £825.08
Getting direct flights for San Francisco...
San Francisco: £540.42
Getting direct flights for Dublin...
No flight data
Dublin: £N/A
No direct flight to Dublin. Looking for indirect flights...
No flight data
Cheapest indirect flight price is: £N/A



---------------------------------------------------------


Microsoft Windows [Version 10.0.19045.6093]
(c) Microsoft Corporation. All rights reserved.

C:\Continuous Learning\100 Days of Code The Complete Python Pro Bootcamp>"C:/Continuous Learning/100 Days of Code The Complete Python Pro Bootcamp/.venv/Scripts/activate.bat"

(.venv) C:\Continuous Learning\100 Days of Code The Complete Python Pro Bootcamp>"C:/Continuous Learning/100 Days of Code The Complete Python Pro Bootcamp/.venv/Scripts/python.exe" "c:/Continuous Learning/100 Days of Code The Complete Python Pro Bootcamp/Day-40-FlightSearchAmadeus/main.py"
{'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
            {'city': 'Frankfurt',
             'iataCode': 'FRA',
             'id': 3,
             'lowestPrice': 42},
            {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
            {'city': 'Hong Kong',
             'iataCode': 'HKG',
             'id': 5,
             'lowestPrice': 551},
            {'city': 'Istanbul',
             'iataCode': 'IST',
             'id': 6,
             'lowestPrice': 320},
            {'city': 'Kuala Lumpur',
             'iataCode': 'KUL',
             'id': 7,
             'lowestPrice': 414},
            {'city': 'New York',
             'iataCode': 'NYC',
             'id': 8,
             'lowestPrice': 240},
            {'city': 'San Francisco',
             'iataCode': 'SFO',
             'id': 9,
             'lowestPrice': 260}]}
Your token is 9MMP3QDa6fQ8jN43FoaXqRtsfOXy
Your token expires in 1799 seconds
sheet_data:
 [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 320, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}]
{
  "price": {
    "iataCode": "PAR",
    "id": 2
  }
}
{
  "price": {
    "iataCode": "FRA",
    "id": 3
  }
}
{
  "price": {
    "iataCode": "TYO",
    "id": 4
  }
}
{
  "price": {
    "iataCode": "HKG",
    "id": 5
  }
}
{
  "price": {
    "iataCode": "IST",
    "id": 6
  }
}
{
  "price": {
    "iataCode": "KUL",
    "id": 7
  }
}
{
  "price": {
    "iataCode": "NYC",
    "id": 8
  }
}
{
  "price": {
    "iataCode": "SFO",
    "id": 9
  }
}
Your email list includes ['narenbagavathye5@gmail.com', 'rakshithasrimathy@gmail.com']
Getting direct flights for Paris...
Paris: £197.22
Getting direct flights for Frankfurt...
Frankfurt: £290.26
Getting direct flights for Tokyo...
Tokyo: £1117.42
Getting direct flights for Hong Kong...
Hong Kong: £1358.22
Getting direct flights for Istanbul...
Istanbul: £318.28
Check your email. Lower price flight found to Istanbul!
SM27f70aec15618f1d6d92b5571a904bf9
Error sending WhatsApp message: 
HTTP Error Your request was:

POST /Accounts/AC4162600d85bbb14581b6ce48a3505b09/Messages.json

Twilio returned the following information:

Unable to create record: Message cannot have the same To and From for account AC4162600d85bbb14581b6ce48a3505b09

More information may be available here:

https://www.twilio.com/docs/errors/63031


Getting direct flights for Kuala Lumpur...
Kuala Lumpur: £982.42
Getting direct flights for New York...
New York: £821.08
Getting direct flights for San Francisco...
San Francisco: £540.42

(.venv) C:\Continuous Learning\100 Days of Code The Complete Python Pro Bootcamp>



--------------------------------------------------------------------------------


Self-Consistency Prompt Engineering Results

---------------------------------------------------------


code:


def warn(*args, **kwargs):
  pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

import anthropic

import os
import anthropic
from dotenv import load_dotenv


load_dotenv()

def llm_model(prompt_txt, params=None):


  # Initialize Anthropic client with environment variable and custom HTTP client
  client = anthropic.Anthropic(
      api_key=os.getenv("ANTHROPIC_API_KEY"),

  )

  # Default parameters for Claude
  default_params = {
      "max_tokens": 256,
      "temperature": 0.5,
      "top_p": 0.2,
      "top_k": 1
  }

  if params:
      default_params.update(params)

  try:
      response = client.messages.create(
          model="claude-sonnet-4-20250514",
          max_tokens=default_params["max_tokens"],
          temperature=default_params["temperature"],
          top_p=default_params["top_p"],
          top_k=default_params["top_k"],
          messages=[
              {
                  "role": "user",
                  "content": prompt_txt
              }
          ]
      )

      # If response.content is a string, return it directly
      if isinstance(response.content, str):
          return response.content
      # If response.content is a list of blocks, join the 'text' from blocks that have it
      elif isinstance(response.content, list):
          return "".join(getattr(block, "text", "") for block in response.content if hasattr(block, "text"))
      else:
          return str(response.content)

  except Exception as e:
      print(f"Error calling Claude API: {e}")
      return None



params = {
"max_new_tokens": 512,
}
prompt = """How to deploy the crewai on crew ai enterprise website without any hassle?
Provide three independent explanations, then determine the most consistent result.
"""
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")



-------------------------

Output:

prompt: How to deploy the crewai on crew ai enterprise website without any hassle?
Provide three independent explanations, then determine the most consistent result.


response : I'll provide three independent explanations for deploying CrewAI on the Crew AI Enterprise platform:

## Explanation 1: Standard Enterprise Deployment Process

**Step-by-step approach:**
1. **Account Setup**: Register for Crew AI Enterprise account and verify your organization
2. **Project Configuration**: Use the web-based dashboard to create a new project and configure your crew structure
3. **Code Integration**: Upload your CrewAI code through the platform's built-in IDE or connect your Git repository
4. **Environment Setup**: Configure environment variables, API keys, and dependencies through the platform interface
5. **Deployment**: Use the one-click deploy button after testing in the staging environment
6. **Monitoring**: Access built-in monitoring and logging tools for production oversight

## Explanation 2: CLI-Based Enterprise Deployment

**Command-line focused approach:**
1. **Install Enterprise CLI**: Download and install the Crew AI Enterprise command-line tools
2. **Authentication**: Run `crew-enterprise login` to authenticate with your enterprise credentials
3. **Project Initialization**: Use `crew-enterprise init` to set up project structure with enterprise templates
4. **Configuration**: Edit the generated `crew-enterprise.yaml` file with your specific crew configurations
5. **Deploy Command**: Execute `crew-enterprise deploy --env production` for direct deployment
6. **Status Verification**: Use `crew-enterprise status` to monitor deployment health

## Explanation 3: Container-Based Enterprise Deployment

**Docker/containerization approach:**
1. **Enterprise Registry Access**: Gain access to Crew AI's private container registry
2. **Base Image**: Pull the enterprise base image: `crew-ai-enterprise:latest`
3. **Custom Configuration**: Create Dockerfile extending the base image with your crew configurations
4. **Platform Integration**: Use the enterprise platform's container deployment service
5. **Scaling Configuration**: Set up auto-scaling rules through the enterprise dashboard
6. **Production Release**: Deploy through the platform's blue-green deployment system

## Most Consistent Result

After analyzing all three explanations, the **most consistent and likely accurate approach** combines elements from all three but emphasizes the **web-based dashboard method (Explanation 1)** as the primary deployment path.

**Recommended hassle-free deployment process:**

1. **Access Enterprise Platform**: Log into your Crew AI Enterprise web dashboard
2. **Use Built-in Tools**: Leverage the platform's integrated development environment and deployment tools
3. **Follow Guided Setup**: Use the platform's step-by-step deployment wizard
4. **Utilize Templates**: Start with enterprise-provided templates for faster setup
5. **One-Click Deploy**: Use the simplified deployment interface rather than complex CLI commands
6. **Monitor Through Dashboard**: Use built-in monitoring rather than external tools

**Key Success Factors:**
- Ensure proper enterprise account permissions
- Have all API keys and environment variables ready
- Test in staging environment first
- Use the platform's native tools rather than external deployment methods

This approach minimizes complexity while leveraging the enterprise platform's designed workflow for the smoothest deployment experience.



----------------------------------------------------------------------------------