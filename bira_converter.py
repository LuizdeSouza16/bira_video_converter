import os
import fnmatch
import sys

if sys.platform  == 'linux':
    command_ffmpeg = 'ffmpeg'
else:
    command_ffmpeg = r'ffmpeg\bin\ffmpeg.exe'

# paramters for ffmpeg
codec_video = '-c:v libx264'
crf = '-crf 24'
preset = '-preset medium'
code_audio = '-c:a aac'
bitrate_audio = '-b:a 128k'

path_input = r'.\videos'
path_output = r'.\output_videos'
parameter = sys.argv

def recursiveConversion(path_input, path_output):
    for root_files, folders, files in os.walk(path_input):
        for file in files:
            if not fnmatch.fnmatch(file, '*.avi'):
                continue
            
            path_file = os.path.join(root_files, file)
            file_name, file_extension = os.path.splitext(file)
            
            output_file = f'{path_output}\\{file_name}.mp4'
            
            command = f'{command_ffmpeg} -i "{path_file}" {codec_video} {crf} {preset} {code_audio}  '\
                f'{bitrate_audio} "{output_file}"'
            
            os.system(command)

def fileConversion(path_input, path_output, video):
        for root_files, folders, files in os.walk(path_input):
            if not fnmatch.fnmatch(video, '*.avi'):
                continue
            
            path_file = f'{path_input}\\{video}'
            file_name, file_extension = os.path.splitext(video)
            
            output_file = f'{path_output}\\{file_name}.mp4'
            
            command = f'{command_ffmpeg} -i "{path_file}" {codec_video} {crf} {preset} {code_audio}  '\
                f'{bitrate_audio} "{output_file}"'
            
            os.system(command)
            

if len(parameter) == 1:
    recursiveConversion(path_input, path_output)
else:
    fileConversion(path_input, path_output, parameter[1])