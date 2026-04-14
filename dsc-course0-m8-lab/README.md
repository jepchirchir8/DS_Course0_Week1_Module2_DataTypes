# Aviation Accident Analysis
# Strategic Aviation Safety Analysis (1983–2023)Client:
 # Airline/Airplane InsurerObjective: Identify low-risk aircraft makes/models and quantify environmental risk factors.
 ## 1. Executive Summary
 This project provides a data-driven risk assessment of commercial and passenger aviation safety. By analyzing historical NTSB data from 1983 to 2023, we identify aircraft makes and models that exhibit superior structural integrity (low destruction rates) and high passenger survivability.\n
 Our analysis separates Large Passenger Models (>=20 occupants) from Small Aircraft (< 20 occupants) to help tailor insurance portfolios toward high-survivability assets and identify critical risk factors that justify premium adjustments.
 ## 2. Methodology & Data Engineering
 To ensure results are statistically robust and commercially relevant, we implemented a rigorous cleaning and transformation pipeline:\n
 Filter Logic: Restricted data to professional builds from 1983 onwards (adhering to the 40-year airframe lifetime rule).\n
 Standardization: Resolved case-sensitivity issues and whitespace in the Make and Model columns to ensure data from manufacturers like "Cessna" and "CESSNA" were aggregated correctly.Statistical Thresholds: Only manufacturers with >=50 incidents and specific models with >=10 incidents were included to prevent outliers from skewing the safety profile.\n
 Calculated Metrics:Injury Rate: \n
 (Fatal + Serious) / Total Occupants$. This normalized score measures survivability regardless of aircraft size.\n
 is_destroyed: A binary indicator (1 or 0) derived from Aircraft.damage to track total hull loss frequency.
 ## 3. Comparative Safety Analysis
 ### Manufacturer (Make) Performance
 Our analysis shows that modern commercial manufacturers (Airbus, Boeing) exhibit a "Zero-Injury Cluster," where the vast majority of accidents involve zero serious injuries.\n
 Large Makes: Boeing, Airbus, and Bombardier consistently show low injury rates (2% - 8%). Specialized makes like DeHavilland demonstrate exceptionally high robustness in this dataset./n
 Small Makes: For general aviation, makes like Maule, Grumman, and Aviat exhibit higher structural integrity compared to standard personal-use aircraft./n
 ### Distribution of Risk
 Small Makes (Violin Plot): The distribution shows that while the safest small makes have a median injury rate of 0.0, they possess a "long tail," indicating that when small aircraft accidents go wrong, the variance in severity is higher.\n
 Large Makes (Strip Plot): Large aircraft show an extreme density at the 0.0 mark. Statistically, an accident in a large commercial jet is far more likely to result in zero serious injuries than an accident in a small prop plane.
 ## 4. Specific Model Recommendations
 Narrowing the scope to specific models with statistically significant sample sizes ($N \ge 10$):SegmentRecommended ModelsPerformance HighlightsLarge FleetBoeing 737-800, Airbus A321, Boeing 777Gold standard for hull integrity and survivability.Small FleetDiamond DA 20, Cessna 180C, Grumman G164BLowest injury metrics in the general aviation segment.
 ## 5. Investigating Risk Variables
 We identified two primary factors that transcend aircraft make and model in determining accident severity.I. Weather Conditions (IMC vs. VMC)Weather remains the single most significant factor in accident survivability.VMC (Visual Conditions): Average injury rates $\approx 21\%$.IMC (Instrument Conditions): Average injury rates jump to over 66%.Insurance Insight: Premiums should be heavily weighted based on the operator's clearance and equipment for IFR (Instrument Flight Rules) operations.II. Engine Type & RedundancyTurbo Fan/Jet: Found on modern jets; these show the lowest injury rates ($\approx 5.8\%$).Reciprocating/Turbo Prop: Common in small planes; these exhibit significantly higher injury rates ($25\%-30\%$).Finding: Multi-engine redundancy and turbine reliability are key indicators of low-risk assets.
 ## 6. Final Recommendations for the Insurer
 Preferred Assets: Prioritize coverage for the Boeing 737 NextGen and Airbus A320/321 families for large fleets. For professional small-scale operations, Diamond Aircraft models provide the best safety-to-risk ratio.Risk Surcharges: We recommend higher premiums for Reciprocating (Piston) Engine aircraft and operators frequently flying in regions with high IMC (Instrument) frequency.Future Mitigation: Encourage a transition toward turbine-powered (Turbo Fan/Prop) aircraft and advanced pilot training in instrument environments to lower overall liability.
 ## 7. Technical Project Structure
 Aviation_Data_Cleaning.ipynb: Data ingestion, filtering, and metric derivation.
 Aviation_EDA_Visuals.ipynb: Statistical analysis, aggregation by Make/Model, and visualization.
 Clean_Aviation_Data.csv: The processed dataset ready for modeling or audit.

