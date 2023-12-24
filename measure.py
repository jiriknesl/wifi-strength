import subprocess
import time
import sys

def get_wifi_strength_macos():
    result = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'agrCtlRSSI' in line:
            return int(line.split(':')[1].strip())

def get_wifi_strength_linux():
    interfaces_result = subprocess.run(["iw", "dev"], capture_output=True, text=True)
    interfaces = [line.split()[1] for line in interfaces_result.stdout.split("\n") if "Interface" in line]

    for interface in interfaces:
        iw_output = subprocess.run(["iw", "dev", interface, "link"], capture_output=True, text=True)
        if "Connected" not in iw_output.stdout or "signal" not in iw_output.stdout:
            continue
        signal = [line.split(":")[1] for line in iw_output.stdout.split("\n") if "signal" in line]
        # Return only the first connected interface
        return int(signal[0].strip().split(" ")[0])

    print("No connected interface found")
    exit(1)

def get_wifi_strength():
    if sys.platform == "darwin":
        return get_wifi_strength_macos()
    elif sys.platform == "linux":
        return get_wifi_strength_linux()
    else:
        print(f"Platform '{sys.platform}' is not supported")
        exit(1)


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
