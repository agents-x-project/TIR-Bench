#gpt-4.1, gpt-4o, o3, o4-mini, o3-tool-using, o4-mini-tool-using
export RUN_NAME="o3-tool-using"
# maze, color, word_search, jigsaw, rotation_game, ocr, refcoco, spot_difference, visual_search, symbolic, math, instrument
export TASK="rotation_game"


# Construct output filename using model and task
OUTPUT_FILE="${RUN_NAME//-/}_${TASK}.txt"


python test.py
# Run the test script and redirect output
#nohup python test.py > "$OUTPUT_FILE" 2>&1 &


