# WiFi Strength

`wifi-strength` is a simple yet effective tool for measuring the signal strength of your WiFi connection in real-time. It provides not only the raw dBm values but also categorizes the strength and compares it with a benchmark.

## Features

- Displays the current WiFi signal strength in dBm.
- Categorizes the signal strength into different levels like Excellent, Strong, Reliable, etc.
- Calculates how many times weaker the current signal is compared to a -30 dBm signal.
- Provides real-time updates every second.

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the `wifi-strength` directory.
3. Run the tool using:

`python measure.py`


4. The output will be displayed in your terminal. Press Ctrl-C to stop the measurement.

## Output Format

The tool prints the WiFi signal strength along with its category and the weakness ratio compared to -30 dBm. The format is:

`<signal_strength> dBm <category>, <weakness_ratio>`


For example:

`-67 dBm Not good, web, e-mail only, 2.00 times weaker than -30 dBm`


## Requirements

- Python 3
- macOS or Linux
- iw on Linux (see https://wireless.wiki.kernel.org/en/users/documentation/iw)

## Author

Jiri Knesl <jiri@flexiana.com>
Jame Ender (https://github.com/JameEnder)

## License

This project is licensed under the MIT License.
