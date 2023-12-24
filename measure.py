import subprocess
import time


def get_wifi_strength():
    result = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'agrCtlRSSI' in line:
            return int(line.split(':')[1].strip())


def categorize_strength(strength):
    if strength > -50:
        return "Excellent"
    elif strength > -60:
        return "Strong, Reliable"
    elif strength > -67:
        return "Strong enough for VoIP, Wifi video"
    elif strength > -70:
        return "Not good, web, e-mail only"
    elif strength > -80:
        return "Bad connection"
    elif strength > -90:
        return "Very bad, barely connected"
    else:
        return "Terrible"


def get_weakness_ratio(strength):
    if strength < -30:
        # Convert the current strength and the -30 dBm benchmark to linear scale (mW)
        current_strength_mW = 10 ** (strength / 10)
        benchmark_strength_mW = 10 ** (-30 / 10)

        # Calculate the weakness ratio
        ratio = benchmark_strength_mW / current_strength_mW
        return f"{ratio:.2f} times weaker than -30 dBm"
    else:
        return "N/A"


def main():
    try:
        while True:
            strength = get_wifi_strength()
            category = categorize_strength(strength)
            weakness_ratio = get_weakness_ratio(strength)
            print(f"{strength} dBm {category}, {weakness_ratio}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Process terminated by user")


if __name__ == "__main__":
    main()
