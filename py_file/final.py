

import os
import time
import numpy as np
import joblib
import cv2
from colorama import Fore, init
from PIL import Image
import mediapipe as mp
import csv
import pandas as pd
from sklearn.preprocessing import StandardScaler
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)



# functions     
            
            
  # loading_bar          

def loading_bar(duration_seconds=5):
    total_iterations = int(duration_seconds / 0.1)  # Calculate the total iterations based on desired duration
    for i in range(total_iterations + 1):  # Adjust the range for the specified duration
        time.sleep(0.1)  # Adjust the sleep time for a slower progression
        percentage_text = "\r\033[93m{}%\033[0m ".format(int((i / total_iterations) * 100))  # Orange text for percentage
        dot_text = "\033[93m|\033[0m"  # Orange text for the dot
        progress_bar = dot_text * int((i / total_iterations) * 50) + " " * (50 - int((i / total_iterations) * 50))  # Creating the progress bar with spaces
        print(percentage_text + progress_bar, end='', flush=True)

    print()  # Move to the next line after the loading bar is complete





def are_you_ready():
    
    print(Fore.GREEN + r"""
.·:''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''':·.
: :     _                                       ____                _         : :
: :    / \   _ __ ___     _   _  ___  _   _    |  _ \ ___  __ _  __| |_   _   : :
: :   / _ \ | '__/ _ \   | | | |/ _ \| | | |   | |_) / _ \/ _` |/ _` | | | |  : :
: :  / ___ \| | |  __/   | |_| | (_) | |_| |   |  _ <  __/ (_| | (_| | |_| |  : :
: : /_/   \_\_|  \___|    \__, |\___/ \__,_|   |_| \_\___|\__,_|\__,_|\__, |  : :
: :                       |___/                                       |___/   : :
'·:...........................................................................:·'
    """)


  # to clear_screen

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# logo lets go

def lets_go():
    print( Fore.GREEN + r"""
              
            ··············································································
            : __       _______ .___________.        _______.           _______   ______  :
            :|  |     |   ____||           |       /       |          /  _____| /  __  \ :
            :|  |     |  |__   `---|  |----`      |   (----`         |  |  __  |  |  |  |:
            :|  |     |   __|      |  |            \   \             |  | |_ | |  |  |  |:
            :|  `----.|  |____     |  |        .----)   |            |  |__| | |  `--'  |:
            :|_______||_______|    |__|        |_______/              \______|  \______/ :
            ··············································································
                 
              """)


# logo lets go2
def lets_go2():
    print( Fore.RED + r"""
              
            ··············································································
            : __       _______ .___________.        _______.           _______   ______  :
            :|  |     |   ____||           |       /       |          /  _____| /  __  \ :
            :|  |     |  |__   `---|  |----`      |   (----`         |  |  __  |  |  |  |:
           -:|--|-----|-----|------|--|------------\---\-------------|--|-|--|-|--|--|--|:
            :|  `----.|  |____     |  |        .----)   |            |  |__| | |  `--'  |:
            :|_______||_______|    |__|        |_______/              \______|  \______/ :
            ··············································································
                 
              """)


    # logo PTA
    
def PTA():
        print(Fore.GREEN +"\n\n   Welcome to", Fore.GREEN + r"""
              
              
    ······················
    :░█▀█░░░░░▀█▀░░░░░█▀█:
    :░█▀▀░░░░░░█░░░░░░█▀█:
    :░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀:
    ······················""")   

    
    # logo  go
def go():
    print(Fore.GREEN + r"""   
                    _____                                                   _____ 
                   ( ___ )                                                 ( ___ )
                    |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
                    |   |  ________  ________          ___  ___  ___        |   | 
                    |   | |\   ____\|\   __  \        |\  \|\  \|\  \       |   | 
                    |   | \ \  \___|\ \  \|\  \       \ \  \ \  \ \  \      |   | 
                    |   |  \ \  \  __\ \  \\\  \       \ \  \ \  \ \  \     |   | 
                    |   |   \ \  \|\  \ \  \\\  \       \ \__\ \__\ \__\    |   | 
                    |   |    \ \_______\ \_______\       \|__|\|__|\|__|    |   | 
                    |   |     \|_______|\|_______|           ___  ___  ___  |   | 
                    |   |                                   |\__\|\__\|\__\ |   | 
                    |   |                                   \|__|\|__|\|__| |   | 
                    |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
                   (_____)                                                 (_____)    

""")
    

# disply main logo
def display_tennis_analytics_logo():
    clear_screen()
    print(Fore.GREEN + """\\
                                        ·····································································
                                        :                    ██████╗  █████╗ ████████╗                       :
                                        :                    ██╔══██╗██╔══██╗╚══██╔══╝                       :
                                        :                    ██████╔╝███████║   ██║                          :
                                        :                    ██╔═══╝ ██╔══██║   ██║                          :
                                        :                    ██║     ██║  ██║   ██║                          :
                                        :                    ╚═╝     ╚═╝  ╚═╝   ╚═╝                          :
                                        :                                                                    :
                                        :        ████████╗███████╗███╗   ██╗███╗   ██╗██╗███████╗            :
                                        :        ╚══██╔══╝██╔════╝████╗  ██║████╗  ██║██║██╔════╝            :
                                        :           ██║   █████╗  ██╔██╗ ██║██╔██╗ ██║██║███████╗            :
                                        :           ██║   ██╔══╝  ██║╚██╗██║██║╚██╗██║██║╚════██║            :
                                        :           ██║   ███████╗██║ ╚████║██║ ╚████║██║███████║            :
                                        :           ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚══════╝            :
                                        :                                                                    :
                                        : █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗████████╗██╗ ██████╗███████╗:
                                        :██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══██╔══╝██║██╔════╝██╔════╝:
                                        :███████║██╔██╗ ██║███████║██║   ╚████╔╝    ██║   ██║██║     ███████╗:
                                        :██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝     ██║   ██║██║     ╚════██║:
                                        :██║  ██║██║ ╚████║██║  ██║███████╗██║      ██║   ██║╚██████╗███████║:
                                        :╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝      ╚═╝   ╚═╝ ╚═════╝╚══════╝:
                                        ····································································     
                                                                                                          __ 
                                                                                              \  /  /|     _)
                                                                                               \/    | #  /__
                               
                                        
                                        """)
 # display hand
    
def hands():
    print("""
                      .+#:                                                .*+.                      
                      *@@@.                                              .@@@#                      
         ..          .@@@@:                                              :@@@@.          ..         
        :%@*.        -@@@@=        :+:                        :+:        =@@@@+        .*@%:        
        -@@@#.       +@@@@*       -@@@:                      -%@@=       +@@@@#.      .*@@@=.       
        :%@@@=.      *@@@@*      :@@@@:                      :%@@@-      +@@@@%.      -@@@@-        
        .*@@@%.     .*@@@@#     .@@@@%.                      .#@@@@.     *@@@@%.     .%@@@#.        
 .       :%@@@=     .*@@@@#     *@@@@-                        :@@@@#     *@@@@#.     -@@@@-         
-@@=.    .#@@@@.    .#@@@@#    -%@@@#.                        .#@@@@-    *@@@@#.    .@@@@%.    .-@@=
:@@@#.    :@@@@#    .#@@@@*   .*@@@@-                          :@@@@#.   +@@@@%.    *@@@@-    .*@@@-
.+@@@*.   .%@@@@-   .#@@@@*   :@@@@*.                          .+@@@@-   =@@@@%.   :@@@@%.   .*@@@*.
 .#@@@*.   :@@@@*.  .#@@@@+   %@@@@-                            -%@@@%   -@@@@%.  .*@@@@-    *@@@#: 
  :@@@@#.  .*@@@@-  .%@@@@=  =@@@@#.                            .*@@@@+  -@@@@%.  -@@@@#.  .#@@@@:  
   :@@@@#.  -@@@@@--#@@@@@@=#@@@@@:                              :@@@@@#=%@@@@@%-:@@@@@=. .#@@@@-   
    -@@@@%==#@@@@@@@@@@@@@@@@@@@@#.                              .*@@@@@@@@@@@@@@@@@@@@%==%@@@@=    
    .=@@@@@@@@@@@@@@@@@@@@@@@@@@@:        ....        ....        :@@@@@@@@@@@@@@@@@@@@@@@@@@@+.    
     .*@@@@@@@@@@@@@@@@@@@@@@@@@@.     .+@@@@@+.    .=@@@@@+.     .@@@@@@@@@@@@@@@@@@@@@@@@@@#.     
      .@@@@@@@@@@@@@@@@@@@@@@@@@@.    :#@@@@*.        .*@@@@%:    .%@@@@@@@@@@@@@@@@@@@@@@@@@:      
       +@@@@@@@@@@@@@@@@@@@@@@@@@.   .#@@@@=            -@@@@#.   .@@@@@@@@@@@@@@@@@@@@@@@@@*       
       -@@@@@@@@@@@@@@@@@@@@@@@@@-  .#@@@@*.            .+@@@@#.  :@@@@@@@@@@@@@@@@@@@@@@@@@-       
       .@@@@@@@@@@@@@@@@@@@@@@@@@@++%@@@@#.              .*@@@@@++@@@@@@@@@@@@@@@@@@@@@@@@@@:       
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.       
        =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                  .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.       
        -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-.                   :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-        
        .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                      :%@@@@@@@@@@@@@@@@@@@@@@@@@@@#.        
         -@@@@@@@@@@@@@@@@@@@@@@@@@@*.                        .+@@@@@@@@@@@@@@@@@@@@@@@@@@=         
         .-@@@@@@@@@@@@@@@@@@@@@@@*.                            .+@@@@@@@@@@@@@@@@@@@@@@@=.         
           .+@@@@@@@@@@@@@@@@@@@+.                                .+@@@@@@@@@@@@@@@@@@@*.           
              .-=--:-=*##%%#*-.                                      .-*#%%%#*=----=-:              
    
"""  )  
    
    
    
  
  
  
  
  
  # Function to print a line followed by two empty lines
def space_out_text():
    print(" ")
    print("_"*40)
    print(" ")

    
    
    

# Function to display the introduction with a cleared screen
def show_intro():
    
    init()  # Initialize colorama for Windows systems
    
   
    
    print(' ')
    print(Style.BRIGHT + "   Welcome to My Final Project!")
    print(' ')
    print("   This project is designed to develop my own skills and evaluate a tennis service.")
    print(' ')
    print("   The objective of this application is to compare a tennis serve with a professional player or a rondom player.")
    print('''
          
          ''')
    
    print("   \nLet's get started!")
    print("=" * 40)
    print(' ')
    are_you_ready()
    time.sleep(5)
    
    
    
    
    
    
# Function to analyze tennis service
def analyze_tennis_service():
    clear_screen()
    PTA()

    print (Fore.GREEN + "   Are you right or left-handed? (R/L): ")
    hands()
    hand_preference = input(Fore.GREEN + "   type (R/L): ")
    
    
    

    if hand_preference.upper() == 'R':
        time.sleep(3)
        clear_screen()
        print(' ')
        print(' ')
        print("  OK nice, So you are a right-handed player.")
        
        lets_go()

        
        print( Fore.LIGHTYELLOW_EX + "      In this Demo version 'pat_v1.2', you will only be able to compare your service with Roger Federer. ")
        print( Fore.LIGHTYELLOW_EX + "             To compare with other players, please upgrade to the pro version.")
        
        
        open_roger_foto()
        
        start_comp_R()
        
        
        
    elif hand_preference.upper() == 'L':
        print("   So you are a left-handed player.")
        
        lets_go2()
        print( Fore.RED + "           Not avaiable in this Demo version 'pat_v1.2'.")
        
        time.sleep(5)
        
        analyze_tennis_service()
      
        
        
        
        
        
    else:
        print("   Invalid input. Please enter 'R' for right-handed or 'L' for left-handed.")





def open_roger_foto():
    # Specify the path to the image file
    script_directory = os.path.abspath(os.path.dirname("D:"))
    image_path = os.path.join(script_directory, 'fig', 'rf1.jpg')

    # Open the image
    image = Image.open(image_path)

    # Display the image (you may need to install an image viewer library for this)
    image.show()

    # Wait for 5 seconds
    time.sleep(3)

  

def start_comp_R():
    
    print("_" * 100)
    print(" ")
    print("   Now you can load your video with your service and compare it with Roger Federer's service.")
    print(" ")
    print("_" * 100)
    print(" ")
    print(" ")
    time.sleep(5)
    

    while True:
        user_video_name = input("  Please write the name of your video (or 'q' to exit): ")

        if user_video_name.lower() == 'q':
            print("  Exiting the program.")
            return

        if os.path.isfile(user_video_name):
            print(" ")
            print(f"  The file '{user_video_name}' was found. Let's analyze it.")
            print("_" * 40)
            print(" ")
            print("   Loading Video...")
            process_video_and_compare(user_video_name)
        else:
            print(" ")
            print(f" you typed {user_video_name}' I'm so sorry but we couldn't find your file. Could you please try again.")
            print(" ")


def process_video_and_compare(user_video_name, csv_new_filename='data_compare.csv',
                              model_filename='model_traind_R_Federer.joblib',
                              result_csv_filename='Data_for_comp.csv'):
    model = joblib.load(model_filename)

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    landmark_indices = [mp_pose.PoseLandmark.NOSE, mp_pose.PoseLandmark.RIGHT_SHOULDER,
                        mp_pose.PoseLandmark.RIGHT_ELBOW, mp_pose.PoseLandmark.RIGHT_WRIST,
                        mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_ELBOW,
                        mp_pose.PoseLandmark.LEFT_WRIST, mp_pose.PoseLandmark.RIGHT_HIP,
                        mp_pose.PoseLandmark.RIGHT_KNEE, mp_pose.PoseLandmark.RIGHT_ANKLE,
                        mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.LEFT_KNEE,
                        mp_pose.PoseLandmark.LEFT_ANKLE]

    landmark_names = [landmark.name for landmark in landmark_indices]

    csv_new_file = open(csv_new_filename, 'w', newline='')
    csv_new_writer = csv.writer(csv_new_file)
    csv_new_writer.writerow(['Frame', 'Landmark Name', 'Landmark ID', 'X', 'Y', 'Z'])

    cap_new = cv2.VideoCapture(user_video_name)

    while cap_new.isOpened():
        ret, frame = cap_new.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            for idx, (landmark_id, landmark_name) in enumerate(zip(landmark_indices, landmark_names)):
                landmark = landmarks[landmark_id]
                h, w, c = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                csv_new_writer.writerow(
                    [cap_new.get(cv2.CAP_PROP_POS_FRAMES), landmark_name, idx, landmark.x, landmark.y, landmark.z])

    csv_new_file.close()

    df_new = pd.read_csv(csv_new_filename)

    X = df_new[['X', 'Y', 'Z']]
    y = df_new['Landmark ID']

    X_new = df_new[['X', 'Y', 'Z']]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_scaled_new = scaler.transform(X_new)

    predictions_new = model.predict(X_scaled_new)

    df_new['Predicted Landmark ID'] = predictions_new.astype(int)

    df_diff = df_new[['Landmark Name', 'Landmark ID', 'Predicted Landmark ID']]
    
    
    # Use .loc to set values in a DataFrame
    df_diff.loc[:, 'Difference'] = df_diff['Landmark ID'] - df_diff['Predicted Landmark ID']


    mean_differences = df_diff.groupby('Landmark Name')['Difference'].mean()
    mean_landmark_values = df_diff.groupby('Landmark Name')['Landmark ID'].mean()
    percentage_mean_differences = (mean_differences / mean_landmark_values) * 100

    percentage_mean_differences_abs = percentage_mean_differences.abs()
    percentage_mean_differences_abs.replace([np.inf, -np.inf], np.nan, inplace=True)
    percentage_mean_differences_abs.dropna(inplace=True)

    similarity_percentage = 100 - percentage_mean_differences_abs



    print("\nLandmark Similarity Summary:")
    for landmark_name, similarity_percent in zip(similarity_percentage.index, similarity_percentage):
        if similarity_percent < 30:
            color = Fore.RED
        elif similarity_percent < 80:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN

        print(" ")
        print(color + f"{landmark_name}: {similarity_percent:.2f}% similar ")

    print(Style.RESET_ALL)  # Reset color after printing




    summary_df = pd.DataFrame({'Landmark Name': similarity_percentage.index,
                                'Similarity Percentage': similarity_percentage})

    video_filename = user_video_name if '/' not in user_video_name else user_video_name.split('/')[-1]
    video_name = os.path.splitext(video_filename)[0]

    summary_filename = f"{video_name}_sum_data.csv"
    summary_df.to_csv(summary_filename, index=False)

    print(f"\nSummary data saved to {summary_filename}.")

    overall_similarity_percent = similarity_percentage.mean()

    if overall_similarity_percent < 40:
        color = Fore.RED

    elif overall_similarity_percent < 70:
        color = Fore.YELLOW
    else:
       color = Fore.GREEN

    print(color + f"\nOverall Similarity:  {overall_similarity_percent:.2f}% similar to the trained model (Roger Federer).")
    print(Style.RESET_ALL)  # Reset color after printing









    
    
 
# ----------------------------------------------------------------------------------------------------------




# Main part of the script
if __name__ == "__main__":
    
    clear_screen()
    while True:
        choice = input("Press 's' to start or 'q' to quit: ").lower()
        
        if choice == 's':
            display_tennis_analytics_logo()
            time.sleep(3)  
                       
            # Display the introduction
            show_intro()

            # Ask the user if they want to analyze their tennis service
            analyze_input = input( Fore.GREEN +  "             (y/n): ")

            # Check the user's input
            if analyze_input.lower() == 'y':
                print(' ' * 40)
                print( '-'*40)
                print(' ' * 40)
                print("Loading ...")
                loading_bar(duration_seconds=5)
                
                
                # If 'y', call the analyze_tennis_service function
                analyze_tennis_service()
            elif analyze_input.lower() == 'n':
                # If 'n', display a message and a space, then close the program
                space_out_text()
                print(Fore.RED +"Program closed.")
            else:
                # If invalid input, display an error message
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        
        
        
        
        
        
                    # Call your function or code to start here
        elif choice == 'q':
            print("Quitting the program...")
            break  # Exit the loop
        else:
            print("Invalid input. Please press 's' to start or 'q' to quit.")
    
