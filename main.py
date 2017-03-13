import os, sys, time

__player_name = ''
__player_name_db = set()


def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.05)


def index():
    os.system('clear')
    delay_print(
    """
    Welcome!
    """)
    time.sleep(1)
    delay_print(
    """
    Be ready, you'll be entering an alternate world that everyone's been
    dreaming about.
    """)
    time.sleep(2)
    delay_print(
    """
    Now, I know you want to experience some adventure once in your life, but before that I need to
    get some Identity that you will be using while you are inside 'THIS' world.
    """)
    time.sleep(2)
    delay_print(
    """
    Did you already have a seperate Identity ready?
    """)
    __player_name = raw_input(
    """
    What's your name?
    """)

    time.sleep(2)

    if __player_name in __player_name_db:
        delay_print(
        """Oops!, It seems that that name is taken already, we are prohibiting dual
        names in this world, in order to be make everyone unique.""")
    __player_name_db.add(__player_name)

    delay_print(
    """
    So your name is """ + __player_name + """ huh?
    """)

    time.sleep(0.5)

    delay_print(
    """
    I see.. """)

    delay_print(
    """
    So lets get started! """)

    time.sleep(1)

    os.system('clear')
index()
