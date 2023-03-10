import os
import fnmatch
import sys

if sys.platform  == 'linux':
    command_ffmpeg = 'ffmpeg'
else:
    command_ffmpeg = r'ffmpeg\bin\ffmpeg.exe'

# paramters for ffmpeg
codec_video = '-c:v libx264'
crf = '-crf 20'
preset = '-preset medium'
code_audio = '-c:a aac'
bitrate_audio = '-b:a 128k'

path_input = r'.\\videos'
path_output = r'.\\output_videos'

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
