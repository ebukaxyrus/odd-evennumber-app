# Multilingual Even or Odd Game

An educational number-parity game with language choices and audio features.

## Technology stack
- Python
- Streamlit
- gTTS

## Confirmed functionality
- Accepts student name and integer input
- checks parity
- includes hard-coded language translations
- offers voice playback for supported options.

## Repository entry point

- `evennumberapp.py`: primary inspected Streamlit application.

## Run locally

```bash
git clone https://github.com/ebukaxyrus/odd-evennumber-app.git
cd odd-evennumber-app
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run evennumberapp.py
```


## Limitations and responsible use

Translations require native-speaker review; some languages have different audio support.

## Documentation and quality checklist

- [ ] Verify clean-environment installation.
- [ ] Add authentic screenshots and demonstration links.
- [ ] Add input/error-handling tests.
- [ ] Check data provenance, licensing and accessibility.

## Author

**Dimakunne Chukwuebuka Francis** · [GitHub](https://github.com/ebukaxyrus) · [Portfolio](https://xyrusportfolio.netlify.app/) · [XY AI Solution](https://xyaisolution.online/)

*Source-reviewed documentation. End-to-end deployment has not been independently verified.*
