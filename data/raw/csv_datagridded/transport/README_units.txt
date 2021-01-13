   The mean and standard deviation of the volume fluxes, temperature fluxes and salt fluxes per unit of horizontal distance can be found in the files transpersta_* .Units are Sv/km (files transpersta_tr_*.txt), TW/km = 10^(12)W/km (files transpersta_ptemp_*.txt), and kg.s^{-1} x 10^7 /km (files transpersta_psalt_*.txt) To get the fluxes along a specific portion of the Extended Ellet Line section these fluxes have to be integrated along the section.

   The mean and standard deviation of the cumultative fluxes (integrated along the section from Iceland) can be found in the files cumtrans_*.txt.  Units are Sv (files cumtrans_tr_*.txt), TW =10^(12)W (files cumtrans_ptemp_*.txt), and  kg.s^{-1} x 10^7 (files cumtrans_psalt_*.txt).

 In all these files the columns are: 
   - Refdist: Distance from Iceland (in km) along the section,
   - Lon: Longitude (degree E),
   - Lat: Latitude (degree N),
   - Water_depth: Maximum depth at the grid point (m),
   - Total: Flux vertically integrated on the whole water column (density > 27.20 kg.m³),
   - Upper_water: Flux vertically integrated for density ranges of [27.20;27.50] kg.m³,
   - Permanent_pycnocline: Flux vertically integrated for density ranges of [27.50;27.70] kg.m³,
   - Labrador_sea_water_level: Flux vertically integrated for density ranges of [27.70;27.85] kg.m³,
   - Overflow_water: Flux vertically integrated for density > 27.85* kg.m³ 

   The number of data points per layer and grid cell can be found in the files transpersta_nbdata.txt and cumtrans_nbdata.txt. These numbers reflect the number of EEL stations used to compute the mean and standard deviation of the transport accross the EEL section.
