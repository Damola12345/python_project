import requests
import sys
import getopt


# send slack message using slack API

def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                            data=payload)
    print(response.text)


def slackbot(argv):

    message = " "

    try:
        opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print('slackbot.py -m <message>')
        sys.exit(1)
    if len(opts) == 0:
        message = "Welcome To Slack!"
    for opt, arg in opts:
        if opt == 'h':
            print('slackbot.py -m <message>')
            sys.exit()
        elif opt in ('-m', '--message'):
            message = arg

    send_slack_message(message)

if __name__ == "__main__":
    slackbot(sys.argv[1:])