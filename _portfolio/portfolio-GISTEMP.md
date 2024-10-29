---
title: "GISS Surface Temperature Anomaly Detection and Analysis (GISTEMP)"
excerpt: <img src='/images/gistemp_spatial_faster.gif' alt='GISTEMP Spatial Plot' width='400' height='400' style='display: block; margin: 0 auto;'>
collection: portfolio
---

GISTEMP, NASA's global temperature analysis system, is the scientific standard for measuring Earth's warming. Temperature anomalies show how much warmer/cooler a region is compared to its typical temperature in a reference period.

I've modernized GISTEMPv4 through:
- Performance: Achieved 2x speed increase through vectorization
- Code Quality: Reduced codebase from ~10,000 to 1,000 lines while maintaining full functionality
- Modernization: Leveraged NumPy, Pandas, and Xarray for improved data handling

The visualization shows global temperature anomalies from 1880-2024, relative to the 1951-1980 baseline.

[GISTEMP Website](https://data.giss.nasa.gov/gistemp/)
