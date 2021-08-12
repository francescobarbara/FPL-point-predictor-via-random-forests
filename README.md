# FPL-point-predictor-via-random-forests
I test a variety of approaches for building a point predictor for Fantasy Premier League. I arranged the data in a "time-series fashion", where I use information available from the previous 4 gameweeks (credit to https://github.com/vaastav/Fantasy-Premier-League for the raw data).

The analysis showed that, among the ML algorithms tested, Random Forests produced the best results. This model can be used for captaincy and transfers choices, and can be easily adapted to predict points on a bigger time-window, becoming also a tool for long-term transfer planning
