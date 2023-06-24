![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Stock-Prophet&fontSize=100&animation=fadeIn&fontAlignY=38&desc=stock%20prediction%20webapp&descAlignY=60&descAlign=75&descSize=20&theme=tokyonight)

This is a web application that provides stock prediction using time series forecasting. It allows users to select a stock dataset and choose the number of years for the forecast. The app retrieves stock data using the Yahoo Finance API and uses the PMDARIMA library for auto ARIMA modeling. The forecasted values and confidence intervals are plotted using Plotly.

## Demo

To try out the Stock Prediction App, visit [https://stock-prophet.streamlit.app/](https://stock-prophet.streamlit.app/).

## Features

- Select from popular stocks like AAPL, GOOG, MSFT, and GME.
- Choose the number of years for the forecast using a slider.
- View raw data and time series plot.
- See the forecasted values and confidence intervals.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

`git clone https://github.com/sailohitaksh-cryptic/Stock--predictor.git`


2. Install the required dependencies:

`pip install -r requirements.txt`

3. Run the app:

`streamlit run main.py`

## Dependencies

- streamlit
- yfinance
- pmdarima
- pandas
- plotly

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

