# Blind Book 📚🔗

Blind Book is a Python-based project designed to map text to Braille using LEDs connected to a Raspberry Pi. The system helps visually impaired individuals interpret text by lighting up LEDs corresponding to Braille patterns.

---

## Features ✨

- **Text-to-Braille Mapping**: Converts text into Braille patterns.
- **LED Indicators**: Lights up LEDs to represent Braille dots for each letter.
- **Multi-Cell Support**: Handles multiple Braille cells to represent longer words.
- **Dynamic Mapping**: Supports Braille patterns for both uppercase and lowercase English alphabets (a-z).

---

## How It Works 🔍

1. The program takes text input (e.g., `"OK"`).
2. Each letter is mapped to a corresponding Braille pattern using a dictionary.
3. LEDs are connected to GPIO pins on the Raspberry Pi, and the pins are activated to represent the Braille pattern for each letter.
4. The LEDs light up to visually simulate the Braille representation of the text.

---

## Tech Stack ⚙️

- **Programming Language**: Python
- **Hardware**:
  - Raspberry Pi (any model with GPIO support)
  - LEDs
  - Resistors and wiring setup
- **Python Libraries**:
  - `gpiozero`: For GPIO pin control.
  - `time`: For managing delays in LED operations.

---
# Future Implementations 🚀

- Replace LEDs with **stepper motors and needles** to create a tactile Braille reading experience.  
- Introduce **multi-language Braille support** for regional and international alphabets.  
- Create a **compact and portable design** with lightweight materials and rechargeable batteries.  

## Installation 🛠️

### Prerequisites

- Raspberry Pi with Raspbian OS installed.
- Python 3.x installed.
- LEDs and necessary wiring setup on the GPIO pins.

### Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/blind-book.git
   cd blind-book
