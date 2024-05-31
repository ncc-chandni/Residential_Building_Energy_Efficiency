## Predicting Energy Efficiency of Residential Building

# Data Set Information: 

Perform energy analysis using 12 different building shapes simulated in Ecotect (Ecotect Software has been used to calculate building's energy consumption by simulating its context within the environment.). The buildings differ with respect to the glazing area, the glazing area distribution, and the orientation, amongst other parameters. We simulate various settings as functions of the afore-mentioned characteristics to obtain 768 building shapes. The dataset comprises 768 samples and 8 features, aiming to predict two real valued responses. It can also be used as a multi-class classification problem if the response is rounded to the nearest integer.

# Attribute Information:

The dataset contains eight attributes (or features, denoted by X1…X8) and two responses (or outcomes, denoted by y1 and y2). The aim is to use the eight features to predict each of the two responses.

Specifically:

X1 Relative Compactness

X2 Surface Area

X3 Wall Area

X4 Roof Area

X5 Overall Height

X6 Orientation

X7 Glazing Area

X8 Glazing Area Distribution

y1 Heating Load

y2 Cooling Load

# PROBLEM STATEMENT

Electrical energy consumption has been increasing over the years as more entities are being electricified day by day. Statistics show that 1/3rd of the energy produced are consumed by Buildings, where people spend most of their time. With increasing demand in energy globally, there is need for efficient use of the energy supplied especially in buildings.

# TECHNICAL OBJECTIVE

Develop a machine learning model to predict cooling energy and heating energy consumption in residential buildings.

# TECHNICAL IMPLICATION OF USING HEATING AND COOLING ENERGY CONSUMPTION PREDICTION MODEL

The use of predictive models for energy consumption can help in optimal sizing of the cooling and heating system in a building thereby improving energy efficiency.

*Energy Savings:* Properly sized heating/cooling systems operate at higher efficiencies, resulting in energy savings and reduced operating costs.

*Reduced Wear and Tear:* Oversized systems often cycle on and off more frequently, which can lead to increased wear and tear on equipment. Right-sizing prevents this issue.

*Comfort:* Systems that are too large may lead to temperature swings and discomfort for occupants. Predictive modeling can help avoid this by ensuring that the system is appropriately sized to maintain consistent comfort.

# ML/DS Goals

Identify missing values and outliers

Explore the data using histogram, boxplots, and barcharts visualizations

Identify important features through univariate and multivariate analysis

Apply Feature Engineering to prepare data for modelling

Build Model

Evaluation of model perfromance
Testing of models
