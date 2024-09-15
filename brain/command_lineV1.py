# all commands
class commands:
    tags = ['news', 'search', 'main', 'self', 'greetings', 'social media', 'normal', 'music', 'calculator', 'accept',
            'reject', 'terminate']
    command_lines = {'commands':
        [
            {'accept': {
                'heard': ["yes", "yaa", "sure", "ok"],
                'say': ["as u say sir", 'as u suggest sir']
            }},
            {'reject': {
                'heard': ['nope', 'no', "don't"],
                'say': ['as you suggest sir', "as you say sir"]
            }},
            {'terminate': {'heard': ['bye', 'bye jarvis', 'terminate', 'turn off jarvis', 'end jarvis'],
                           'say': ['bye sir']}},
                {'news': {
            'heard': ['top news', 'tell me todays headlines', 'what are the top news', 'headlines',
                      'what are top headlines', 'what is happening around the world',
                      'what are progress in science', 'what are progress in tech',
                      'can you tell me about todays update', 'what are the updates'],
            'say': ['As you say Sir']
        }},
            {'search': {'heard': ['google', 'open google', 'start google', 'run google',
                                  'youtube', 'open youtube', 'start youtube', 'run youtube', 'who is',
                                  'what is', 'search on google',
                                  'hey jarvis can you open google', 'can you open google'],
                        'say': ['opening search']}},
            {'main':
                 {'heard': ['jarvis', 'wake up jarvis', 'wake up', 'are you up jarvis', 'are you up',
                            'oh i see', 'hey jarvis wake up', 'wake up buddy', 'hey jarvis'],
                  'say': ['yes sir']}},
            {'self': {'heard': ['who are you', 'what are you', 'who is jarvis'],
                      'say': ['I am Jarvis your personal assistant',
                              'I am personal assistant named jarvis']}},
            {'greetings':
                 {'heard': ['hi', 'hello', 'hey', 'hi jarvis', 'hello jarvis', 'good morning',
                            'good night', 'good afternoon', 'good evening', 'hey jarvis'],
                  'say': ['hi sir', 'hello sir']}},
            {'social media': {
                'heard': ['whatsapp', 'facebook', 'twitter', 'social media', 'open facebook',
                          'open whatsapp', 'open twitter', 'open linkedin', 'linkedin', 'instagram',
                          'hey jarvis can you open whatsapp'],
                'say': ['initializing social media']}},
            {'normal': {
                'heard': ['current time', "what's the time",
                          'what is time', 'tell me current time', 'can you tell me whats the time'],
                'say': ["okay sir"]}},
            {'music': {
                'heard': ['play music', 'song', 'music', 'sound', 'turn on music',
                          'can you play some song', 'drop some beats',
                          'can you play some music', 'can you play some sound', 'play next song',
                          'play previous song', 'play previous music',
                          'play next music', 'stop music', 'stop sound', 'stop song', 'pause music',
                          'pause sound', 'pause song', 'I want to listen some music', 'i want to listen music',
                          'i want music',],
                'say': ['sure sir']
            }},
            {'calculator': {
                'heard': ["math", "calculator", "calci", 'open calculator', 'start calculator',
                          'open calci', 'start calci', 'start math mode', 'initialize math mode',
                          'initialize calculator', 'initialize calculator mode'],
                'say': ['initializing math mode', 'starting calculator', 'shifting to math mode',
                        'shifting to calculation mode', 'initializing calculator']}}
        ]}

