import streamlit as st
import base64
import plotly.express as px

quiz_data = {
    "Addition": {
        "easy": [
            {"question": "What is 1 + 1?", "options": ["0", "1", "2", "3"], "correct_answer": "2"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correct_answer": "4"},
            {"question": "What is 3 + 4?", "options": ["5", "6", "7", "8"], "correct_answer": "7"},
            {"question": "What is 5 + 3?", "options": ["7", "8", "9", "10"], "correct_answer": "8"},
            {"question": "What is 7 + 2?", "options": ["8", "9", "10", "11"], "correct_answer": "9"},
            {"question": "What is 4 + 6?", "options": ["8", "9", "10", "11"], "correct_answer": "10"},
            {"question": "What is 8 + 3?", "options": ["10", "11", "12", "13"], "correct_answer": "11"},
            {"question": "What is 6 + 5?", "options": ["10", "11", "12", "13"], "correct_answer": "11"},
            {"question": "What is 9 + 4?", "options": ["11", "12", "13", "14"], "correct_answer": "13"},
            {"question": "What is 10 + 2?", "options": ["10", "11", "12", "13"], "correct_answer": "12"}
        ],
        "medium": [
            {"question": "What is 15 + 28?", "options": ["43", "42", "41", "44"], "correct_answer": "43"},
            {"question": "What is 37 + 14?", "options": ["49", "50", "51", "52"], "correct_answer": "51"},
            {"question": "What is 62 + 19?", "options": ["80", "81", "82", "83"], "correct_answer": "81"},
            {"question": "What is 46 + 35?", "options": ["80", "81", "82", "83"], "correct_answer": "81"},
            {"question": "What is 54 + 29?", "options": ["83", "82", "81", "84"], "correct_answer": "83"},
            {"question": "What is 68 + 23?", "options": ["89", "91", "92", "90"], "correct_answer": "91"},
            {"question": "What is 73 + 18?", "options": ["89", "90", "91", "92"], "correct_answer": "91"},
            {"question": "What is 52 + 47?", "options": ["99", "98", "97", "96"], "correct_answer": "99"},
            {"question": "What is 85 + 15?", "options": ["100", "101", "102", "103"], "correct_answer": "100"},
            {"question": "What is 39 + 64?", "options": ["102", "103", "104", "101"], "correct_answer": "103"}
           
        ],
        "hard": [
            {"question": "What is 124 + 276?", "options": ["400", "398", "401", "402"], "correct_answer": "400"},
            {"question": "What is 345 + 689?", "options": ["1032", "1033", "1031", "1040"], "correct_answer": "1034"},
            {"question": "What is 458 + 342?", "options": ["800", "810", "811", "812"], "correct_answer": "800"},
            {"question": "What is 512 + 478?", "options": ["989", "990", "991", "992"], "correct_answer": "990"},
            {"question": "What is 734 + 269?", "options": ["1003", "1002", "1001", "1004"], "correct_answer": "1003"},
            {"question": "What is 876 + 543?", "options": ["1419", "1420", "1421", "1422"], "correct_answer": "1419"},
            {"question": "What is 960 + 741?", "options": ["1700", "1701", "1702", "1703"], "correct_answer": "1701"},
            {"question": "What is 1234 + 876?", "options": ["2110", "2111", "2112", "2113"], "correct_answer": "2110"},
            {"question": "What is 3456 + 7890?", "options": ["11345", "11346", "11347", "11344"], "correct_answer": "11346"},
            {"question": "What is 6789 + 5432?", "options": ["12221", "12220", "12222", "12223"], "correct_answer": "12221"}
            
        ]
    },
    "Subtraction": {
        "easy": [
             {"question": "What is 5 - 2?", "options": ["1", "2", "3", "4"], "correct_answer": "3"},
             {"question": "What is 9 - 3?", "options": ["5", "6", "7", "8"], "correct_answer": "6"},
             {"question": "What is 8 - 4?", "options": ["2", "3", "4", "5"], "correct_answer": "4"},
             {"question": "What is 6 - 1?", "options": ["4", "5", "6", "7"], "correct_answer": "5"},
             {"question": "What is 10 - 7?", "options": ["1", "2", "3", "4"], "correct_answer": "3"},
             {"question": "What is 7 - 3?", "options": ["3", "4", "5", "6"], "correct_answer": "4"},
             {"question": "What is 4 - 2?", "options": ["1", "2", "3", "4"], "correct_answer": "2"},
             {"question": "What is 9 - 5?", "options": ["2", "3", "4", "5"], "correct_answer": "4"},
             {"question": "What is 3 - 1?", "options": ["0", "1", "2", "3"], "correct_answer": "2"},
             {"question": "What is 8 - 6?", "options": ["1", "2", "3", "4"], "correct_answer": "2"}
        ],
        
        "medium": [
            {"question": "What is 23 - 15?", "options": ["6", "7", "8", "9"], "correct_answer": "8"},
            {"question": "What is 35 - 19?", "options": ["15", "16", "17", "18"], "correct_answer": "16"},
            {"question": "What is 52 - 27?", "options": ["24", "25", "26", "27"], "correct_answer": "25"},
            {"question": "What is 47 - 29?", "options": ["17", "18", "19", "20"], "correct_answer": "18"},
            {"question": "What is 68 - 32?", "options": ["34", "35", "36", "37"], "correct_answer": "36"},
            {"question": "What is 74 - 46?", "options": ["27", "28", "29", "30"], "correct_answer": "28"},
            {"question": "What is 83 - 55?", "options": ["26", "27", "28", "29"], "correct_answer": "28"},
            {"question": "What is 96 - 49?", "options": ["45", "46", "47", "48"], "correct_answer": "47"},
            {"question": "What is 61 - 37?", "options": ["23", "24", "25", "26"], "correct_answer": "24"},
            {"question": "What is 89 - 63?", "options": ["25", "26", "27", "28"], "correct_answer": "26"}
        ],
        "hard": [
            {"question": "What is 124 - 76?", "options": ["48", "49", "50", "51"], "correct_answer": "48"},
            {"question": "What is 289 - 145?", "options": ["141", "142", "143", "144"], "correct_answer": "144"},
            {"question": "What is 372 - 198?", "options": ["172", "173", "174", "175"], "correct_answer": "174"},
            {"question": "What is 456 - 239?", "options": ["215", "216", "217", "218"], "correct_answer": "217"},
            {"question": "What is 549 - 287?", "options": ["260", "261", "262", "263"], "correct_answer": "262"},
            {"question": "What is 638 - 293?", "options": ["344", "345", "346", "347"], "correct_answer": "345"},
            {"question": "What is 721 - 376?", "options": ["343", "344", "345", "346"], "correct_answer": "345"},
            {"question": "What is 847 - 419?", "options": ["426", "427", "428", "429"], "correct_answer": "428"},
            {"question": "What is 953 - 567?", "options": ["384", "385", "386", "387"], "correct_answer": "386"},
            {"question": "What is 1047 - 689?", "options": ["357", "358", "359", "360"], "correct_answer": "358"}
        ]
    },
    "Multiplication": {
        "easy": [
            {"question": "What is 2 × 3?", "options": ["4", "5", "6", "7"], "correct_answer": "6"},
            {"question": "What is 4 × 5?", "options": ["15", "20", "25", "30"], "correct_answer": "20"},
            {"question": "What is 3 × 3?", "options": ["6", "7", "8", "9"], "correct_answer": "9"},
            {"question": "What is 6 × 2?", "options": ["8", "10", "12", "14"], "correct_answer": "12"},
            {"question": "What is 7 × 1?", "options": ["5", "6", "7", "8"], "correct_answer": "7"},
            {"question": "What is 8 × 4?", "options": ["28", "32", "36", "40"], "correct_answer": "32"},
            {"question": "What is 5 × 2?", "options": ["5", "10", "15", "20"], "correct_answer": "10"},
            {"question": "What is 9 × 3?", "options": ["24", "27", "30", "33"], "correct_answer": "27"},
            {"question": "What is 10 × 0?", "options": ["0", "5", "10", "15"], "correct_answer": "0"},
            {"question": "What is 7 × 2?", "options": ["12", "14", "16", "18"], "correct_answer": "14"}
        ],
        
        "medium": [     
            {"question": "What is 12 × 4?", "options": ["42", "44", "46", "48"], "correct_answer": "48"},
            {"question": "What is 9 × 7?", "options": ["60", "63", "66", "69"], "correct_answer": "63"},
            {"question": "What is 8 × 6?", "options": ["42", "46", "48", "50"], "correct_answer": "48"},
            {"question": "What is 11 × 5?", "options": ["50", "55", "60", "65"], "correct_answer": "55"},
            {"question": "What is 14 × 3?", "options": ["38", "40", "42", "44"], "correct_answer": "42"},
            {"question": "What is 7 × 8?", "options": ["54", "56", "58", "60"], "correct_answer": "56"},
            {"question": "What is 6 × 9?", "options": ["52", "54", "56", "58"], "correct_answer": "54"},
            {"question": "What is 13 × 4?", "options": ["50", "52", "54", "56"], "correct_answer": "52"},
            {"question": "What is 15 × 2?", "options": ["28", "30", "32", "34"], "correct_answer": "30"},
            {"question": "What is 10 × 10?", "options": ["90", "95", "100", "105"], "correct_answer": "100"}
        ],
        "hard": [
            {"question": "What is 17 × 12?", "options": ["194", "200", "204", "208"], "correct_answer": "204"},
            {"question": "What is 14 × 15?", "options": ["200", "205", "210", "215"], "correct_answer": "210"},
            {"question": "What is 19 × 13?", "options": ["243", "245", "247", "249"], "correct_answer": "247"},
            {"question": "What is 18 × 11?", "options": ["198", "200", "204", "208"], "correct_answer": "198"},
            {"question": "What is 16 × 14?", "options": ["220", "224", "228", "232"], "correct_answer": "224"},
            {"question": "What is 15 × 17?", "options": ["250", "255", "260", "265"], "correct_answer": "255"},
            {"question": "What is 20 × 13?", "options": ["250", "255", "260", "265"], "correct_answer": "260"},
            {"question": "What is 22 × 15?", "options": ["320", "325", "330", "335"], "correct_answer": "330"},
            {"question": "What is 21 × 18?", "options": ["370", "374", "378", "382"], "correct_answer": "378"},
            {"question": "What is 23 × 19?", "options": ["430", "435", "437", "441"], "correct_answer": "437"}
        ]
    },
    "Division": {
        "easy": [
            {"question": "What is 10 ÷ 2?", "options": ["4", "5", "6", "7"], "correct_answer": "5"},
            {"question": "What is 16 ÷ 4?", "options": ["2", "3", "4", "5"], "correct_answer": "4"},
            {"question": "What is 9 ÷ 3?", "options": ["2", "3", "4", "5"], "correct_answer": "3"},
            {"question": "What is 20 ÷ 5?", "options": ["2", "3", "4", "5"], "correct_answer": "4"},
            {"question": "What is 18 ÷ 6?", "options": ["1", "2", "3", "4"], "correct_answer": "3"},
            {"question": "What is 8 ÷ 2?", "options": ["2", "3", "4", "5"], "correct_answer": "4"},
            {"question": "What is 15 ÷ 3?", "options": ["4", "5", "6", "7"], "correct_answer": "5"},
            {"question": "What is 14 ÷ 7?", "options": ["1", "2", "3", "4"], "correct_answer": "2"},
            {"question": "What is 12 ÷ 4?", "options": ["2", "3", "4", "5"], "correct_answer": "3"},
            {"question": "What is 25 ÷ 5?", "options": ["4", "5", "6", "7"], "correct_answer": "5"}
        ],
        
        "medium": [
            {"question": "What is 36 ÷ 6?", "options": ["5", "6", "7", "8"], "correct_answer": "6"},
            {"question": "What is 49 ÷ 7?", "options": ["5", "6", "7", "8"], "correct_answer": "7"},
            {"question": "What is 64 ÷ 8?", "options": ["6", "7", "8", "9"], "correct_answer": "8"},
            {"question": "What is 81 ÷ 9?", "options": ["7", "8", "9", "10"], "correct_answer": "9"},
            {"question": "What is 56 ÷ 8?", "options": ["6", "7", "8", "9"], "correct_answer": "7"},
            {"question": "What is 45 ÷ 5?", "options": ["7", "8", "9", "10"], "correct_answer": "9"},
            {"question": "What is 32 ÷ 4?", "options": ["6", "7", "8", "9"], "correct_answer": "8"},
            {"question": "What is 63 ÷ 7?", "options": ["8", "9", "10", "11"], "correct_answer": "9"},
            {"question": "What is 24 ÷ 3?", "options": ["6", "7", "8", "9"], "correct_answer": "8"},
            {"question": "What is 72 ÷ 9?", "options": ["7", "8", "9", "10"], "correct_answer": "8"}
        ],
        "hard": [
            {"question": "What is 144 ÷ 12?", "options": ["10", "11", "12", "13"], "correct_answer": "12"},
            {"question": "What is 169 ÷ 13?", "options": ["12", "13", "14", "15"], "correct_answer": "13"},
            {"question": "What is 196 ÷ 14?", "options": ["12", "13", "14", "15"], "correct_answer": "14"},
            {"question": "What is 225 ÷ 15?", "options": ["13", "14", "15", "16"], "correct_answer": "15"},
            {"question": "What is 256 ÷ 16?", "options": ["14", "15", "16", "17"], "correct_answer": "16"},
            {"question": "What is 289 ÷ 17?", "options": ["15", "16", "17", "18"], "correct_answer": "17"},
            {"question": "What is 324 ÷ 18?", "options": ["16", "17", "18", "19"], "correct_answer": "18"},
            {"question": "What is 361 ÷ 19?", "options": ["17", "18", "19", "20"], "correct_answer": "19"},
            {"question": "What is 400 ÷ 20?", "options": ["18", "19", "20", "21"], "correct_answer": "20"},
            {"question": "What is 441 ÷ 21?", "options": ["19", "20", "21", "22"], "correct_answer": "21"}
        ]
    }
    
}


st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/file-mathematical-operations-1-638-1611041488.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }}
    
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.3);
        z-index: 0;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Rest of your Streamlit app code goes here

def show_question():
    question = quiz_data[st.session_state.selected_topic][st.session_state.selected_level][st.session_state.current_question]
    st.write(f"Question {st.session_state.current_question + 1}: {question['question']}")
    selected_option = st.radio("Select your answer:", question['options'], key=f"option_{st.session_state.current_question}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous", key="previous"):
            previous_question()
    with col2:
        if st.session_state.current_question < len(quiz_data[st.session_state.selected_topic][st.session_state.selected_level]) - 1:
            if st.button("Next", key="next"):
                next_question()
        else:
            if st.button("Complete Quiz", key="complete"):
                check_answer(selected_option)
                st.session_state.quiz_completed = True
                st.session_state.page = "final_score"
                st.experimental_rerun()

    if not st.session_state.quiz_completed:
        if st.button("Submit"):
            check_answer(selected_option)

# Function to check the selected answer
def check_answer(selected_option):
    question = quiz_data[st.session_state.selected_topic][st.session_state.selected_level][st.session_state.current_question]
    if selected_option == question["correct_answer"]:
        st.write("Correct!")
        st.balloons()
        st.session_state.score += 1
    else:
        st.write("Incorrect!")
    st.write(f"Explanation: {question['correct_answer']}")

# Function to move to the next question
def next_question():
    if st.session_state.current_question < len(quiz_data[st.session_state.selected_topic][st.session_state.selected_level]) - 1:
        st.session_state.current_question += 1
        st.experimental_rerun()  # Rerun to show the next question

# Function to move to the previous question
def previous_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1
        st.experimental_rerun()  # Rerun to show the previous question

# Function to display the final score and buttons
def show_final_page():
    st.markdown(f"<h1 style='text-align: center; color: white; font-size: 72px;'>Your Score: {st.session_state.score}/{len(quiz_data[st.session_state.selected_topic][st.session_state.selected_level])}</h1>", unsafe_allow_html=True)

    # Buttons for "New Game" and "End"
    col1, col2 = st.columns(2)
    with col1:
        if st.button("New Game", key="new_game"):
            st.session_state.selected_topic = None
            st.session_state.selected_level = None
            st.session_state.quiz_completed = False
            st.session_state.score = 0
            st.session_state.current_question = 0
            st.session_state.page = "choose_topic"
            st.experimental_rerun()

    with col2:
        if st.button("End", key="end"):
            st.session_state.page = "end"
            st.experimental_rerun()

# Function to display the thank-you page
def show_end_page():
    st.markdown("<h1 style='text-align: center; color: white;'>Thank You for Using the Math Quiz!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>We hope you enjoyed the quiz!</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Keep practicing, and see you next time!</h3>", unsafe_allow_html=True)
    st.image("https://www.example.com/thank_you_image.png", use_column_width=True)  # Add a creative image (replace the URL with your image URL)

# Main function
def main():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'selected_topic' not in st.session_state:
        st.session_state.selected_topic = None
    if 'selected_level' not in st.session_state:
        st.session_state.selected_level = None
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    if 'page' not in st.session_state:
        st.session_state.page = "welcome"  # Default to welcome page

    if st.session_state.page == "welcome":
        st.title("Welcome to Math Quiz")
        if st.button("Start"):
            st.session_state.page = "choose_topic"
            st.experimental_rerun()

    elif st.session_state.page == "choose_topic":
        st.title("Choose a Topic")
        topic = st.selectbox("Select a topic:", ["Addition", "Subtraction", "Multiplication", "Division"])
        level = st.selectbox("Select a level:", ["easy", "medium", "hard"])
        if st.button("Proceed"):
            st.session_state.selected_topic = topic
            st.session_state.selected_level = level
            st.session_state.current_question = 0
            st.session_state.page = "quiz"
            st.experimental_rerun()

    elif st.session_state.page == "quiz":
        if st.session_state.selected_topic and not st.session_state.quiz_completed:
            show_question()

    elif st.session_state.page == "final_score":
        show_final_page()

    elif st.session_state.page == "end":
        show_end_page()

if __name__ == "__main__":
    main()
