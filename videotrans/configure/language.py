# -*- coding: utf-8 -*-
translate_language = {
    "zh": {
        "selectmp4": "选择视频",
        "selectsavedir": "选择翻译后存储目录",
        "proxyerrortitle": "代理错误",
        "proxyerrorbody": "无法访问google服务，请正确设置代理",
        "softname": "视频字幕翻译和配音",
        "anerror": "出错了",
        "selectvideodir": "必须选择视频",
        "sourenotequaltarget": "源语言和目标语言不得相同",
        "shoundselecttargetlanguage": "必须选择一个目标语言",
        "running": "执行中",
        "ing": "执行中",
        "exit": "退出",
        "end": "已结束",
        "stop": "已停止(点击开始)",
        "subtitleandvoice_role": "你没有选择视频，只输入了字幕，将仅仅创建配音wav文件，请确认继续？",
        "waitrole":"正在获取可用配音角色，请稍等重新选择",
        "downloadmodel":"模型不存在，请去下载后存放到:",
        "modelpathis":"当前模型路径是:",
        "modellost":"模型下载出错或者下载不完整，请重新下载后存放到 models目录下",
        "embedsubtitle":"硬字幕嵌入",
        "softsubtitle":"软字幕",
        "nosubtitle":"不添加字幕",
        "baikeymust":"你必须填写百度key",
        "chatgptkeymust":"你必须填写chatGPT key",
        "waitsubtitle":"等待编辑字幕(点击继续合成)",
        "waitforend":"正在合成视频",
        "createdirerror":"创建目录失败",
        "processingstatusbar":"正在处理视频:[{var1}],还有[{var2}]个在等待处理",
        "confirmstop":"确认停止执行?如果字幕生成一半，再次启动可能不完整，可以手动删掉tmp目录",
        "deepl_authkey":"你必须填写DeepL的授权key",
        "deepl_nosupport":"DeepL不支持翻译为该语言",
        "wait_edit_subtitle":"等待修改字幕",
        "continue_action":"继续下一步",
        "autocomposing":"秒倒计时后将自动合成视频，修改字幕编辑区任意内容后将停止倒计时",
        "queding":"确定",
        "hechengchucuo":"合成出错，缺少文件:",
        "installffmpeg":"未找到 ffmpeg，软件不可用，请去 ffmpeg.org 下载并加入到系统环境变量",
        "yinsekelong":"音色克隆将接入 github.com/jianchang512/clone-voice ，实现自定义音色配音",
        "yinsekaifazhong":"音色克隆开发中",
        "whisper_type_all":"整体识别",
        "whisper_type_split":"预先分割",
        "waitclear":"正在关闭后台进程",
        "subtitle_tips":" 在此可编辑字幕信息，或拖动已有srt文件到此处松开 ",
        "setdeepl_authkey":"必须设置DeepL 授权token",
        "setdeeplx_address":"必须设置你的 DeepLX 地址和端口，比如 127.0.0.1:1188",
        "mustberole":"必须选择一个配音角色",
        "qingqueren":"请确认",
        "only_srt":"没有选择目标语言，不会进行翻译和配音，仅从视频中提取字幕srt文件到目录文件夹，点Yes将继续执行，否则取消",
        "tencent_key":"必须填写腾讯 SecretId 和 SecretKey",
        "xuanzejuese":"必须选择配音角色，请先根据字幕语言选择目标语言，然后选择配音角色", 
        
        
        "daoruzimu":"导入字幕", 
        "shitingpeiyin":"试听配音", 
        "xianqidongrenwu":"先启动任务，待字幕翻译完成后可试听,配音速度、自动加速实时修改生效", 
        "juanzhu":" 请考虑捐助软件，帮助软件保持更新维护！ ", 
        "nocuda":'你的设备不满足CUDA加速要求，请确认是NVIDIA显卡，并已配置好CUDA环境，可去仓库说明页面查看安装方法,然后重启软件', 
        "noselectrole":"未选择角色，不可试听", 
        "chongtingzhong":'重听中', 
        "shitingzhong":'试听中/点击重听', 
        "bukeshiting":'无字幕内容，不可试听', 
        "kaishichuli":"开始处理", 
        "tiquzimu":"原始语言设为视频发音语言，目标语言设为想翻译为的语言", 
        "kaishitiquhefanyi":"开始提取和翻译", 
        "tiquzimuno":"原始语言设为视频发音语言", 
        "kaishitiquzimu":"开始提取字幕", 
        "kaishihebing":"开始合并", 
        "zimu_video":"选择要合并的视频，将字幕srt文件拖拽到右侧字幕区", 
        "zimu_peiyin":"请将目标语言设为字幕所用语言，并选择配音角色", 
        "kaishipeiyin":"开始配音", 
        "anzhuangvlc":"你可能需要先安装VLC解码器，", 
        "jixuzhong":"继续执行中", 
        "daojishitingzhi":"倒计时停止，修改后请手动点击“继续执行”按钮", 
        "nextstep":"继续下一步", 
        "tianxieazure":"必须填写Azure key", 
        "bencijieshu":"本次任务结束", 
        "kaishichuli":"开始处理...", 
        "yunxingbukerole":'运行中，不可改为无配音角色', 
        "bixutianxie":"必须填写", 
        "peiyinmoshisrt":'配音模式下必须选择配音角色、目标语言、并将本地srt字幕文件拖拽到右侧字幕区', 
        "hebingmoshisrt":'合并模式下，必须选择视频、字幕嵌入类型、并将字幕srt文件拖拽到右侧字幕区', 
        "fanyimoshi1":'必须选择要翻译到的目标语言', 
        "bukedoubucunzai": '视频和字幕不能同时都不存在哦！', 
        "wufapeiyin":'没有选择目标语言，无法进行配音哦，请选择目标语言或取消配音角色', 
        "xuanzeyinpinwenjian":"选择音视频文件", 
        "vlctips":"拖动视频到此或者双击选择视频", 
        "vlctips2":" 安装VLC解码器后可预览播放", 
        "xuanzeyinshipin":"点击选择或拖拽音频、视频文件到此处", 
        "tuodongdaoci":"拖动要转换的文件到此处松开", 
        "tuodongfanyi":"拖动要翻译的文本文件或srt文件到此处松开", 
        "zhixingwc":"执行完成", 
        "zhixinger":"执行出错", 
        "starttrans":"开始翻译", 
        "yinpinhezimu": "音频和字幕至少要选择一个", 
        "bixuyinshipin":"必须选择有效的音视频文件", 
        "chakanerror":"识别前预处理失败，请确认视频中是否含有音频数据", 
        "srtisempty":"字幕内容为空", 
        "savesrtto":"选择保存字幕文件到..", 
        "neirongweikong":"内容不能为空", 
        "yuyanjuesebixuan":"语言和角色必须选择", 
        "nojueselist":"未获取到角色列表", 
        "buzhichijuese":"不支持该语音角色", 
        "nowenjian":"不存在有效文件", 
        "yinpinbuke":"音频不可转为", 
        "quanbuend":"全部转换完成", 
        "wenbenbukeweikong":"待翻译文本不可为空", 
        "buzhichifanyi":"不支持翻译到该目标语言", 
        "ffmpegno":"未找到 ffmpeg，软件不可用，请去 ffmpeg.org 下载并加入到系统环境变量", 
        "newversion":"有新的版本可以下载了", 
        "tingzhile":"停止了", 
        "geshihuazimuchucuo":"格式化字幕文件出错", 
        "moweiyanchangshibai":"末尾添加延长视频帧失败，将保持原样不延长视频", 
        "xiugaiyuanyuyan":"等待修改原语言字幕/继续", 
        "jimiaohoufanyi":"秒后自动翻译，你可以停止倒计时后去修改字幕，以便翻译更准确", 
        "xiugaipeiyinzimu":"等待修改配音字幕/点击继续", 
        "zidonghebingmiaohou":"秒后自动合并，你可以停止倒计时后去修改字幕，以便配音更准确", 
        "jieshutips":"视频处理结束:相关素材可在目标文件夹内查看，含字幕文件、配音文件等", 
        "mubiao":"打开输出文件夹",
        "endandopen":"已完成，点击打开 ",
        "waitforstart":"等待开始",


        "xianxuanjuese":"请先选择TTS类型和角色",
        "shezhijueseline":"填写使用该角色配音的行数,例如 2,3,7,8"
    },
    "en": {
        "continue_action":"继续下一步",
        "xuanzejuese":"must to be select dubbing role, frist select subtitle language and select dubbing role",
        "tencent_key":"must be input tencent's SecretId and SecretKey",
        "qingqueren":"Please confirm",
        "only_srt":"Not select target language，will only create srt file，click Yes to continue,else cancel",
        "mustberole":"must be selet role for listen",
        "setdeepl_authkey":"must be set DeepL token",
        "setdeeplx_address":"must be set DeepLX address and port",
        "subtitle_tips":" Edit subtitle here or drap srt file to here ",
        "waitclear":"closing process",
        "whisper_type_all":"whole",
        "whisper_type_split":"first split",
        "processingstatusbar":"Process video:[{var1}] total, [{var2}] waitting",
        "yinsekelong": "Timbre cloning will use github.com/jianchang512/clone-voice. These features will then be used as the voice for dubbing characters, achieving custom dubbing with any desired timbre.",
        "yinsekaifazhong": "Timbre cloning is under development.",
        "installffmpeg":"ffmpeg not found, the software is not available. Please download it from ffmpeg.org and add it to the system's environment variables.",
        "hechengchucuo":"Composing video error，lost file:",
        "queding":"Confirm",
        "wait_edit_subtitle":"Wait for edit subtitle",
        "autocomposing":" seconds After the countdown, the video will be automatically synthesized. After modifying any content in the subtitle editing area, the countdown will stop",
        "deepl_nosupport":"DeepL don't support translation to the language",
        "deepl_authkey":"You need an DeepL authentication key",
        "confirmstop":"Stop this task?",
        "prcoessingstatusbar":"Processing video: [{var1}], with [{var2}] waiting to be processed",
        "createdirerror":"create dir error",
        "waitforend":"Composing video",
        "waitsubtitle":"Wait edit subtitle(click for continue)",
        "baikeymust":"input your baidu key",
        "chatgptkeymust":"input your chatgpt key",
        "nosubtitle":"No Subtitle",
        "embedsubtitle":"Embed subtitle",
        "softsubtitle":"Soft subtitle",
        "modellost":"There is an error in the model download or the download is incomplete. Please re-download and store it in the models directory.",
        "modelpathis":"Model storage path:",
        "downloadmodel":"Model does not exist, download it and save to:",
        "waitrole":"getting voice role list,hold on",
        "selectsavedir": "select an dir for output",
        "selectmp4": "select an mp4 video",
        "subtitleandvoice_role": "no video and has subtitle at edit area,will create dubbing audio wav files,confirm for continue?",
        "proxyerrortitle": "Proxy Error",
        "shoundselecttargetlanguage": "Must select a target language ",
        "proxyerrorbody": "Failed to access Google services. Please set up the proxy correctly.",
        "softname": "Video Subtitle Translation and Dubbing",
        "anerror": "An error occurred",
        "selectvideodir": "You must select the video to be translated",
        "sourenotequaltarget": "Source language and target language must not be the same",
        "running": "Running",
        "ing": "Running",
        "exit": "Exit",
        "end": "Ended",
        "stop": "Stop(click start)", 
        
        "daoruzimu":"Import subtitles", 
"shitingpeiyin":"Trial dubbing", 
"xianqidongrenwu":"Firstly start the task, you can listen to it after the subtitle translation is completed, the dubbing speed and auto-acceleration take effect in real time", 
"juanzhu":" Please consider donating to the software to keep it updated and maintained! ", 
"nocuda":"Your device does not meet CUDA acceleration requirements, please confirm it is an NVIDIA graphics card and CUDA environment has been configured, you can go to the repository description page to view the installation method, and then restart the software", 
"noselectrole":"No role selected, cannot trial listening", 
"chongtingzhong":"Re-listening", 
"shitingzhong":"Listening/Click to re-listen", 
"bukeshiting":"No subtitle content, cannot trial listening", 
"kaishichuli":"Start processing", 
"tiquzimu":"Set the original language to the language voiced in the video, the target language is the language you want to translate to", 
"kaishitiquhefanyi":"Start extracting and translating", 
"tiquzimuno":"Set the original language to the language voiced in the video", 
"kaishitiquzimu":"Start extracting subtitles", 
"kaishihebing":"Start merging", 
"zimu_video":"Choose the video to be merged, drag and drop the subtitles srt file to the right subtitle area", 
"zimu_peiyin":"Please set the target language as the language used for subtitles and select the dubbing role", 
"kaishipeiyin":"Start voiceover", 
"anzhuangvlc":"You may need to install the VLC decoder first,", 
"jixuzhong":"Continue executing", 
"daojishitingzhi":"Countdown stops, after modifying, please manually click the 'Continue Execution' button", 
"nextstep":"Move on to the next step", 
"tianxieazure":"Must fill in Azure key", 
"bencijieshu":"This task is over", 
"kaishichuli":"Start processing...", 
"yunxingbukerole":"Running, cannot change to without dubbing role", 
"bixutianxie":"Must fill in", 
"peiyinmoshisrt":"Must choose a dubbing role, target language in dubbing mode, and drag and drop the local srt subtitle file to the right subtitle area", 
"hebingmoshisrt":"In merge mode, you must select a video, subtitle embedding type, and drag and drop the subtitles srt file to the right subtitle area", 
"fanyimoshi1":"Must choose the target language to translate to", 
"bukedoubucunzai": "Videos and subtitles cannot be non-existent at the same time!", 
"wufapeiyin":"No target language selected, can't dubbing, please select target language or cancel dubbing role", 
"xuanzeyinpinwenjian":"Select audio and video files", 
"vlctips":"Drag the video here or double-click to select the video", 
"vlctips2":"Can preview and play after installing VLC decoder", 
"xuanzeyinshipin":"Click to select or drag and drop audio, video files here", 
"tuodongdaoci":"Drag the file to be converted here and release", 
"tuodongfanyi":"Drag the text file or srt file to be translated here and release", 
"zhixingwc":"Execution completed", 
"zhixinger":"Execution error", 
"starttrans":"Start translating", 
"yinpinhezimu":"At least one of audio and subtitles must be selected", 
"bixuyinshipin":"Must select a valid audio and video file", 
"chakanerror":"Pre-processing failed before recognition, please confirm if there is audio data in the video", 
"srtisempty":"The subtitle content is empt", 
"savesrtto":"Choose to save the subtitle file to..", 
"neirongweikong":"Content cannot be empty", 
"yuyanjuesebixuan":"Language and role must be selected", 
"nojueselist":"Did not get the role list", 
"buzhichijuese":"This voice role is not supported", 
"nowenjian":"No valid files exist", 
"yinpinbuke":"Audio cannot be converted to", 
"quanbuend":"All conversions are done", 
"wenbenbukeweikong":"The text to be translated cannot be empty", 
"buzhichifanyi":"Does not support translation to the target language", 
"ffmpegno":"ffmpeg not found, the software is not available, please download from ffmpeg.org and add to system environment variables", 
"newversion":"There is a new version to download", 
"tingzhile":"Stopped", 
"geshihuazimuchucuo":"Formatting subtitle file error", 
"moweiyanchangshibai":"Failed to add extension video frames at the end, will maintain the original state without extending the video", 
"xiugaiyuanyuyan":"Wait to modify original language subtitles / continue", 
"jimiaohoufanyi":"Automatically translated in seconds, you can stop the countdown to modify the subtitles so that the translation is more accurate", 
"xiugaipeiyinzimu":"Wait to modify the dubbed subtitles / click continue", 
"zidonghebingmiaohou":"Automatically merge in seconds, you can stop the countdown to modify the subtitles so that the dubbing is more accurate", 
"jieshutips":"Video processing ends: Relevant materials can be found in the target folder, including subtitle files, voiceover files, etc",
        "mubiao":"Open output folder",
        "endandopen":"Ended click to open ",
        "waitforstart":"Wait for starting",
        "xianxuanjuese":"Please select TTS type and role first",
        "shezhijueseline":"Fill in the number of lines using the character's voice acting, eg. 2,3,7,8"
    }
}


#  名称: google翻译代码，字幕语言代码，百度翻译代码，deep代码,腾讯代码
language_code_list={
    "zh":{
        "中文简": ['zh-cn', 'chi','zh','ZH','zh'],
        "中文繁": ['zh-tw', 'chi','cht','ZH','zh-TW'],
        "英语": ['en', 'eng','en','EN-US','en'],
        "法语": ['fr', 'fre','fra','FR','fr'],
        "德语": ['de', 'ger','de','DE','de'],
        "日语": ['ja', 'jpn','jp','JA','ja'],
        "韩语": ['ko', 'kor','kor','KO','ko'],
        "俄语": ['ru', 'rus','ru','RU','ru'],
        "西班牙语": ['es', 'spa','spa','ES','es'],
        "泰国语": ['th', 'tha','th','No','th'],
        "意大利语": ['it', 'ita','it','IT','it'],
        "葡萄牙语": ['pt', 'por','pt','PT','pt'],
        "越南语": ['vi', 'vie','vie','No','vi'],
        "阿拉伯语": ['ar', 'are','ara','No','ar'],
        "土耳其语": ['tr', 'tur','tr','tr','tr'],
    },
    "en":{
        "Simplified_Chinese": ['zh-cn', 'chi','zh','ZH','zh'],
        "Traditional_Chinese": ['zh-tw', 'chi','cht','ZH','zh-TW'],
        "English": ['en', 'eng','en','EN-US','en'],
        "French": ['fr', 'fre','fra','FR','fr'],
        "German": ['de', 'ger','de','DE','de'],
        "Japanese": ['ja', 'jpn','jp','JA','ja'],
        "Korean": ['ko', 'kor','kor','KO','ko'],
        "Russian": ['ru', 'rus','ru','RU','ru'],
        "Spanish": ['es', 'spa','spa','ES','es'],
        "Thai": ['th', 'tha','th','No','th'],
        "Italian": ['it', 'ita','it','IT','it'],
        "Portuguese": ['pt', 'por','pt','PT','pt'],
        "Vietnamese": ['vi', 'vie','vie','No','vi'],
        "Arabic": ['ar', 'are','ara','No','ar'],
        "Turkish": ['tr', 'tur','tr','tr','tr'],
    }
}

# cli language ccode
clilanglist = {
    "zh-cn": ['zh-cn', 'chi'],
    "zh-tw": ['zh-tw', 'chi'],
    "en": ['en', 'eng'],
    "fr": ['fr', 'fre'],
    "de": ['de', 'ger'],
    "ja": ['ja', 'jpn'],
    "ko": ['ko', 'kor'],
    "ru": ['ru', 'rus'],
    "es": ['es', 'spa'],
    "th": ['th', 'tha'],
    "it": ['it', 'ita'],
    "pt": ['pt', 'por'],
    "vi": ['vi', 'vie'],
    "ar": ['ar', 'are'],
    "tr": ['tr', 'tur'],
}
