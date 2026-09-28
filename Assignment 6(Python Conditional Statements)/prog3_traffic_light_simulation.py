"""
Program 3: Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
"""

def traffic_light(color):
    color_clean = color.strip().lower()
    
    if color_clean == "red":
        action = "Stop"
    elif color_clean == "yellow":
        action = "Wait"
    elif color_clean == "green":
        action = "Go"
    else:
        action = "Invalid Signal!"
        
    print(f"Traffic Light: {color:<10} -> Action: {action}")
    return action


def main():
    print("--- Program 3: Traffic Light Simulator ---")
    
    signals = ["Red", "Yellow", "Green", "Blue"]
    for sig in signals:
        traffic_light(sig)


if __name__ == "__main__":
    main()
