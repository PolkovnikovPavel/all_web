import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name) as f:
            lines = f.readlines()
        result = []
        for i in range(len(lines)):
            line = lines[i]
            if len(line) <= frame_width:
                result.append(line)
            else:
                while len(line) > frame_width:
                    result.append(line[:frame_width])
                    line = line[frame_height:]
                    if len(result) == frame_height:
                        break
                if len(result) < frame_height:
                    result.append(line)
            if len(result) == frame_height:
                break
        return '\n'.join(result)
    except Exception as e:
        raise e


parser = argparse.ArgumentParser()
parser.add_argument("--frame-height", type=int)
parser.add_argument("--frame-width", type=int)
parser.add_argument('file_name')

args = parser.parse_args()
frame_height = args.frame_height
frame_width = args.frame_width
file_name = args.file_name


print(format_text_block(frame_height, frame_width, file_name))
