# Geospatial Intelligence Portfolio
### Jose Escobar · Geospatial Intelligence & Automation Engineer

End-to-end geospatial intelligence systems — satellite imagery pipelines, PostGIS spatial databases, environmental monitoring platforms, computer vision on aerial datasets, and LiDAR terrain analysis. Ten documented sprints from UAV telemetry foundations through live production platforms querying real Hansen GFC, MODIS, WDPA, and Sentinel-2 data.

**CV:** [goheist01.github.io/jose-escobar-cv](https://goheist01.github.io/jose-escobar-cv)  
**Contact:** jaemaciel.55@gmail.com  
**Stack:** Python · PostgreSQL/PostGIS · Google Earth Engine · Sentinel-2 · MODIS · Hansen GFC · WDPA · YOLOv8 · GeoPandas · Supabase · Leaflet.js · GDAL · AWS S3 · LiDAR · rasterio

---

## Sprint Log

| Sprint | Title | Stack | Output |
|--------|-------|-------|--------|
| 01 | PX4 SITL Environment Setup (macOS arm64) | PX4 · jMAVSim · QGroundControl | Environment |
| 02 | UAV Failsafe Validation + Mission Analysis | pyulog · pandas · MAVLink · PX4 | [5 analyses →](https://goheist01.github.io/uav-mission-intelligence/notebooks/sprint02_failsafe_signal_loss.html) |
| 03 | Orthomosaic + NDVI (Valley Parkway, Ohio) | WebODM · OpenDroneMap · rasterio | [Analysis →](https://goheist01.github.io/uav-mission-intelligence/notebooks/sprint03_orthomosaic_aukerman.html) |
| 04 | Multispectral Agriculture (Sentinel-2 · Jalisco) | GEE · stackstac · rasterio | [Analysis →](https://goheist01.github.io/uav-mission-intelligence/notebooks/sprint04_multispectral_agriculture.html) |
| 05A | Solar Thermal Inspection Pipeline | OpenCV · scikit-image · pandas | [Analysis →](https://goheist01.github.io/uav-mission-intelligence/notebooks/sprint05a_solar_thermal_inspection.html) |
| 05B | Solar Thermal Triage Dashboard | OpenCV · pandas · HTML/JS | [Dashboard →](https://goheist01.github.io/uav-mission-intelligence/outputs/dashboard/) |
| 06 | LiDAR Point Cloud + DTM/DSM (Utah Capitol) | laspy · rasterio · NumPy | [Analysis →](https://goheist01.github.io/uav-mission-intelligence/notebooks/sprint06_lidar_structure_detection.html) |
| 07 | GEE Land Cover Classification (Jalisco) | GEE · Random Forest · geemap | [Analysis →](https://goheist01.github.io/uav-mission-intelligence/outputs/sprint07_gee_land_cover.html) |
| 08 | YOLOv8 Solar Panel Fault Detection | YOLOv8 · PyTorch · Transfer Learning · T4 GPU | [Analysis →](https://goheist01.github.io/uav-mission-intelligence/notebooks/sprint08_solar_panel_detection.html) |
| 09 | Amazon Deforestation Intelligence Platform | PostGIS · Supabase · Hansen GFC · MODIS · WDPA · Leaflet | [**LAUNCH →**](https://goheist01.github.io/uav-mission-intelligence/outputs/amazon_platform.html) |
| 10 | Mekong Delta Agricultural Intelligence Platform | Sentinel-2 · gdal2tiles · AWS S3 · PostGIS · Supabase · Chart.js | [**LAUNCH →**](https://goheist01.github.io/uav-mission-intelligence/outputs/mekong_platform.html) |

---

## Live Platforms

### Sprint 09 — Amazon Deforestation Intelligence Platform
**[LAUNCH PLATFORM →](https://goheist01.github.io/uav-mission-intelligence/outputs/amazon_platform.html)**

Live PostGIS database on Supabase. 1,121 real forest loss pixels from Hansen GFC v1.11 across Para, Amazonas, Mato Grosso, and Rondônia (2001–2023). Loss drivers from MODIS MCD12Q1 post-loss land cover — published INPE/GFW proxy methodology. 370 WDPA v2024 registered protected area boundaries. 66 confirmed violations detected via `ST_Within()` spatial intersection. Leaflet.js frontend with satellite/dark basemap toggle, year/driver/violation filters, and click-to-detail sidebar.

```
Hansen GFC v1.11 · MODIS MCD12Q1 · WDPA v2024
PostgreSQL 17 + PostGIS 3.6 · Supabase · Leaflet.js
```

---

### Sprint 10 — Mekong Delta Agricultural Intelligence Platform
**[LAUNCH PLATFORM →](https://goheist01.github.io/uav-mission-intelligence/outputs/mekong_platform.html)**

Five Sentinel-2 SR composites (Nov 2022–Apr 2023, SCL cloud mask) served as 23,245 XYZ tiles (zoom 7–13) from GitHub Pages — band switching is instant. COG files on AWS S3. PostGIS database on Supabase: 499 agricultural parcels across 13 Vietnamese provinces + Kandal and Prey Veng (Cambodia), 4,981 spectral observations across 4 rice seasons. Rice paddy flood cycle confirmed in NDWI data — December peak (0.464), May (0.324), September (0.185) matching the real Mekong three-crop calendar.

```
Sentinel-2 SR · GDAL · gdal2tiles · AWS S3 · GitHub Pages
PostgreSQL 17 + PostGIS 3.6 · Supabase · Leaflet.js · Chart.js
```

---

## Data Methodology

This portfolio prioritizes verifiable data over impressive-looking but unsubstantiated outputs. Where synthetic or modeled data is used, it is explicitly labeled.

**Real data used across sprints:**
- Hansen GFC v1.11 — real 30m forest loss pixel coordinates, loss years, canopy cover
- MODIS MCD12Q1 — real post-loss land cover classification per pixel
- WDPA v2024 — real UN-registered protected area polygon boundaries
- Sentinel-2 SR Harmonized — real satellite imagery via Google Earth Engine
- InfraredSolarModules — real thermal drone imagery benchmark dataset (ICLR 2020)
- USGS/OpenTopography LiDAR — real classified point cloud data
- Planetary Computer Sentinel-2 L2A — real multispectral imagery

**Synthetic data explicitly labeled:**
- Sprint 10 parcel boundaries — synthetic grid polygons on real province coordinates. No public cadastral registry exists for Mekong Delta at individual parcel level.
- Sprint 10 spectral observations — values derived from published spectral profile ranges, not pixel-sampled per individual parcel.

---

## Repository Structure

```
uav-mission-intelligence/
├── notebooks/          # Jupyter notebooks + HTML exports per sprint
├── outputs/            # Platform HTML, visualization PNGs
│   ├── tiles/          # Sentinel-2 XYZ tiles (Sprint 10)
│   └── dashboard/      # Thermal triage dashboard (Sprint 05B)
├── data/               # Source datasets (GeoJSON, CSV, COG)
└── README.md
```

---

## Environment Setup

```bash
# Clone repo
git clone https://github.com/goheist01/uav-mission-intelligence.git
cd uav-mission-intelligence

# Create conda environment
conda create -n uav-env python=3.11
conda activate uav-env

# Install dependencies
pip install geopandas rasterio stackstac pystac-client \
    laspy sqlalchemy psycopg2-binary boto3 \
    matplotlib pandas numpy scikit-learn \
    ultralytics jupyter
```

**Python:** 3.11 · **PostgreSQL:** 17 (local, port 5433) · **PostGIS:** 3.6

---

*Every sprint is publicly documented and verifiable. Portfolio maintained at [goheist01.github.io/jose-escobar-cv](https://goheist01.github.io/jose-escobar-cv)*
