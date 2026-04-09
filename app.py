from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Brewster Madrid Classroom Locator", page_icon="📍", layout="wide")
    
st.markdown(
    """
    <style>
    
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background: radial-gradient(1000px 500px at 8% -15%, #20345a 0%, #10192b 50%, #0b101b 100%);
        color: #f7f9fc;
        font-family: 'Manrope', sans-serif;
    }
        font-family: Georgia, "Times New Roman", serif;
    h1, h2, h3 {
        color: #f7f9fc;
    }

    h1 {
        font-family: 'Cinzel', serif;
        letter-spacing: 0.06em;
    }

    p, div, span, label {
        color: #f7f9fc;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #131b2f 0%, #101726 100%);
        border-right: 1px solid #223150;
    }

        font-family: Georgia, "Times New Roman", serif;
        color: #eef3ff !important;
    }

    .card {
        background: linear-gradient(160deg, rgba(26, 37, 61, 0.95) 0%, rgba(17, 24, 40, 0.95) 100%);
        border: 1px solid rgba(117, 144, 196, 0.35);
        border-radius: 20px;
        padding: 1.2rem 1.3rem;
        margin-top: 0.6rem;
        margin-bottom: 0.8rem;
    }

    .subtitle {
        color: #d0dcf6;
        font-size: 1.02rem;
        margin-top: -0.2rem;
    }

    .welcome-title {
        font-family: 'Cinzel', serif;
        font-size: 1.85rem;
        font-weight: 800;
        color: #f7f9fc;
        margin-bottom: 0.35rem;
        letter-spacing: 0.06em;
    }

    .big-question {
        font-size: 1.04rem;
        font-weight: 500;
        color: #f7f9fc;
        line-height: 1.75;
        color: #dbe5fb;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Floor configuration keeps logic centralized and avoids repeated condition checks.
FLOOR_CONFIG = {
    "First Floor": {
        "prefix": "P",
        "classrooms": ["P11", "P12", "P13", "P14", "P15", "P16"],
        "map": Path("assets/maps/first_floor.png"),
    },
    "Ground Floor": {
        "prefix": "PG",
        "classrooms": ["PG1", "PG2", "PG3", "PG4"],
        "map": Path("assets/maps/ground_floor.png"),
    },
    "Basement": {
        "prefix": "PB",
        "classrooms": ["PB1", "PB2", "PB3"],
        "map": Path("assets/maps/basement.png"),
    },
}
CLASSROOM_DETAILS = {
    "P11": {
        "floor": "First Floor",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the main stairs up to the First Floor.", "Turn left to find P11."],
    },
    "P12": {
        "floor": "First Floor",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs to the First Floor.", "Walk straight to the left along the central corridor to find P12."],
    },
    "P13": {
        "floor": "First Floor",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs to the First Floor.", "Walk straight along the central corridor to reach the end and find P13."],
    },
    "P14": {
        "floor": "First Floor",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs to the First Floor.", "Continue down the central corridor to the right to find P14."],
    },
    "P15": {
        "floor": "First Floor",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs to the First Floor.", "Turn right and walk straight to find P15."],
    },
    "P16": {
        "floor": "First Floor",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs to the First Floor.", "Turn right and walk straight, and you will find P16 against the wall by the stairs."],
    },
    "PG1": {
        "floor": "Ground Floor",
        "steps": ["Enter through the main entrance.", "Stay on the Ground Floor.", "Walk straight and turn right to find PG1, it is in the library."],
    },
    "PG2": {
        "floor": "Ground Floor",
        "steps": ["Enter through the main entrance.", "Stay on the Ground Floor.", "Continue along the central hallway to PG2."],
    },
    "PG3": {
        "floor": "Ground Floor",
        "steps": ["Enter through the main entrance.", "Remain on the Ground Floor.", "Walk straight and make a right to enter the library, and you should see PG3."],
    },
    "PG4": {
        "floor": "Ground Floor",
        "steps": ["Enter through the main entrance.", "Stay on the Ground Floor.", "PG4 will be on the right near the enterance of the Palecete and infront of the boy´s bathroom."],
    },
    "PB1": {
        "floor": "Basement",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs down to the Basement.", "PB1 should be on the left once you reach the Basement."],
    },
    "PB2": {
        "floor": "Basement",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs down to the Basement.", "Walk straight to the middle hallway and PB2 will be straight ahead."],
    },
    "PB3": {
        "floor": "Basement",
        "steps": ["Enter through the main entrance.", "Walk straight and turn left to take the stairs to go down to the Basement.", "Once down the stairs, PB3 will be on the right."],
    },
}


if "section" not in st.session_state:
    st.session_state.section = "Classroom Helper"


def go_to_section(section_name: str) -> None:
    st.session_state.section = section_name
    st.rerun()


section = st.session_state.section


if section == "Classroom Helper":
    st.markdown("<h1 style='text-align: center;'>Brewster Madrid Classroom Locator</h1>", unsafe_allow_html=True)
    st.markdown(
    "<p class='subtitle' style='text-align: center;'>An easy way to instantly locate classrooms, floors, and directions.</p>",
        unsafe_allow_html=True,
    )
    st.write("")

    with st.container(border=True):
        st.markdown(
            """
            <div class="card">
                <div class="welcome-title">Welcome to Brewster Madrid!</div>
                <div class="big-question">We’re so excited to have you here. Starting somewhere new can feel overwhelming, so I’m here to help. If you need assistance finding a classroom, just click below.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Yes, I need help finding a classroom", type="primary"):
            go_to_section("Find a Classroom")


if section == "Find a Classroom":
    st.header("Find a Classroom")
    classroom_input = st.text_input("Enter your classroom (example: P11, PG3, PB2)")

    if classroom_input:
        classroom_code = classroom_input.strip().upper().replace(" ", "")
        if classroom_code not in CLASSROOM_DETAILS:
            st.error("That classroom is not one of the rooms in this building.")
        else:
            details = CLASSROOM_DETAILS[classroom_code]
            detected_floor = details["floor"]
            st.success(f"{classroom_code} is located on: {detected_floor}")

            floor_map = FLOOR_CONFIG[detected_floor]["map"]

            map_col, directions_col = st.columns([1.35, 1], gap="large")

            with map_col:
                st.subheader(f"{detected_floor} Map")
                if floor_map.exists():
                    st.image(str(floor_map), use_container_width=True)
                else:
                    st.warning(
                        "Map image not found. Add file at "
                        f"{floor_map}"
                    )

            with directions_col:
                with st.container(border=True):
                    st.subheader("Classroom Information")
                    st.write(f"Classroom: {classroom_code}")
                    st.write(f"Floor: {details['floor']}")
                    st.write("Directions:")
                    for step_number, step in enumerate(details["steps"], start=1):
                        st.write(f"{step_number}. {step}")

    st.write("")
    if st.button("Back to Main Tab"):
        go_to_section("Classroom Helper")

