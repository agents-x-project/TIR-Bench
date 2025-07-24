import json
def get_task_params(model, task):
    if task=='maze':
        file_path = '/home/ming/tool-using-data/maze_data/maze_collect.json'
        save_path = f'/home/ming/tool-using-data/maze_data/maze_collect_{model}.json'
        image_path = '/home/ming/tool-using-data/maze_data/'
    elif task=='color':
        file_path = '/home/ming/tool-using-data/colorbench/color.json'
        save_path = f'/home/ming/tool-using-data/colorbench/color_{model}.json'
        image_path = '/home/ming/tool-using-data/colorbench/'
    elif task=='word_search':
        file_path = '/home/ming/tool-using-data/word_search/word_search_collection.json'
        save_path = f'/home/ming/tool-using-data/word_search/word_search_collection_{model}.json'
        image_path = '/home/ming/tool-using-data/word_search/'
    elif task=='jigsaw':
        file_path = '/home/ming/tool-using-data/jigsaw_data/jigsaw_collect.json'
        save_path = f'/home/ming/tool-using-data/jigsaw_data/jigsaw_collect_{model}.json'
        image_path = '/home/ming/tool-using-data/jigsaw_data/'
    elif task=='rotation_game':
        file_path = '/home/ming/tool-using-data/rotation_game/rotation_collect.json'
        save_path = f'/home/ming/tool-using-data/rotation_game/rotation_collect_{model}.json'
        image_path = '/home/ming/tool-using-data/rotation_game/'
    elif task=='ocr':
        file_path = '/home/ming/tool-using-data/ocr_data/ocr_collect.json'
        save_path = f'/home/ming/tool-using-data/ocr_data/ocr_collect_{model}.json'
        image_path = '/home/ming/tool-using-data/ocr_data/'
    elif task=='refcoco':
        file_path = '/home/ming/tool-using-data/refcoco/refcoco.json'
        save_path = f'/home/ming/tool-using-data/refcoco/refcoco_{model}.json'
        image_path = '/home/ming/tool-using-data/refcoco/'
    elif task=='spot_difference':
        file_path = '/home/ming/tool-using-data/spot_difference/spot_difference_collection.json'
        save_path = f'/home/ming/tool-using-data/spot_difference/spot_difference_collection_{model}.json'
        image_path = '/home/ming/tool-using-data/spot_difference/'
    elif task=='visual_search':
        file_path = '/home/ming/tool-using-data/visual_search/visual_search_collect.json'
        save_path = f'/home/ming/tool-using-data/visual_search/visual_search_collect_{model}.json'
        image_path = '/home/ming/tool-using-data/visual_search/'
    elif task=='symbolic':
        file_path = '/home/ming/tool-using-data/symbolicVisualPuzzle/symbolic_collection.json'
        save_path = f'/home/ming/tool-using-data/symbolicVisualPuzzle/symbolic_collection_{model}.json'
        image_path = '/home/ming/tool-using-data/symbolicVisualPuzzle/'
    elif task=='math':
        file_path = '/home/ming/tool-using-data/function/math_collection.json'
        save_path = f'/home/ming/tool-using-data/function/math_collection_{model}.json'
        image_path = '/home/ming/tool-using-data/function/'
    elif task=='contrast':
        file_path = '/home/ming/tool-using-data/contrast_image/contrast_collection.json'
        save_path = f'/home/ming/tool-using-data/contrast_image/contrast_collection_{model}.json'
        image_path = '/home/ming/tool-using-data/contrast_image/'
    elif task=='instrument':
        file_path = '/home/ming/tool-using-data/instrument_reading/instrument_reading_collect.json'
        save_path = f'/home/ming/tool-using-data/instrument_reading/instrument_reading_collect_{model}.json'
        image_path = '/home/ming/tool-using-data/instrument_reading/'

    else:
        raise Exception("In correct task name.")
    return file_path, save_path.replace('-boyue', ''), image_path




def check_file(task, model):
    test_model = model

    if task == 'maze':
        path1 = f'/home/ming/tool-using-data/maze_data/maze_collect_{test_model}.json'
        path = f'/home/ming/tool-using-data/maze_data/maze_collect.json'
    elif task == 'color':
        path1 = f'/home/ming/tool-using-data/colorbench/color_{test_model}.json'
        path = f'/home/ming/tool-using-data/colorbench/color.json'
    elif task == 'word_search':
        path = '/home/ming/tool-using-data/word_search/word_search_collection.json'
        path1 = f'/home/ming/tool-using-data/word_search/word_search_collection_{model}.json'
    elif task == 'jigsaw':
        path = '/home/ming/tool-using-data/jigsaw_data/jigsaw_collect.json'
        path1 = f'/home/ming/tool-using-data/jigsaw_data/jigsaw_collect_{model}.json'
    elif task == 'rotation_game':
        path = '/home/ming/tool-using-data/rotation_game/rotation_collect.json'
        path1 = f'/home/ming/tool-using-data/rotation_game/rotation_collect_{model}.json'
    elif task == 'ocr':
        path = '/home/ming/tool-using-data/ocr_data/ocr_collect.json'
        path1 = f'/home/ming/tool-using-data/ocr_data/ocr_collect_{model}.json'
    elif task == 'refcoco':
        path = '/home/ming/tool-using-data/refcoco/refcoco.json'
        path1 = f'/home/ming/tool-using-data/refcoco/refcoco_{model}.json'
    elif task == 'spot_difference':
        path = '/home/ming/tool-using-data/spot_difference/spot_difference_collection.json'
        path1 = f'/home/ming/tool-using-data/spot_difference/spot_difference_collection_{model}.json'
    elif task == 'visual_search':
        path = '/home/ming/tool-using-data/visual_search/visual_search_collect.json'
        path1 = f'/home/ming/tool-using-data/visual_search/visual_search_collect_{model}.json'
    elif task == 'symbolic':
        path = '/home/ming/tool-using-data/symbolicVisualPuzzle/symbolic_collection.json'
        path1 = f'/home/ming/tool-using-data/symbolicVisualPuzzle/symbolic_collection_{model}.json'
    elif task == 'math':
        path = '/home/ming/tool-using-data/function/math_collection.json'
        path1 = f'/home/ming/tool-using-data/function/math_collection_{model}.json'
    elif task=='contrast':
        path = '/home/ming/tool-using-data/contrast_image/contrast_collection.json'
        path1 = f'/home/ming/tool-using-data/contrast_image/contrast_collection_{model}.json'
    elif task=='instrument':
        path = '/home/ming/tool-using-data/instrument_reading/instrument_reading_collect.json'
        path1 = f'/home/ming/tool-using-data/instrument_reading/instrument_reading_collect_{model}.json'

    else:
        raise Exception("Incorrect task name.")

    print(path1,path)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(path1, 'r', encoding='utf-8') as f:
            data1 = json.load(f)
    except:
        print(f'wrong {task}, model: {model}')
        return False

        # print( model)

    keys = data1.keys()
    if len(data) != len(data1):
        print(f'wrong number of task {task}, expected number is {len(data)}, exact number is {len((data1))}')
        return False
    for key in keys:
        item = data1[key]
        if item['model_response'] == None or len(item['model_response']) == 0:
            print(f"task: {task}, model: {model}, number: {key}, answer is {item['model_response']}")
            return False
    return True