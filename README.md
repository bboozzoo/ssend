# ssend - simple Slack integration helper

The purpose of `ssend` tool is to provide a simple interface for
sending Slack messages from command line. What could have been done
with a single `curl` oneline has been done in couple of lines of
Python code. Hopefully this can be considered an example on Python to
Slack integration.

## Configuration

Necessary configuration can be passed via command line (see `--help`),
or via environment (`SLACK_WEBHOOK_URL`) so everything should be easy
if you heppen to integrate this with a CI service like Jenkins.

Alternatively, `ssend` will look for user configuration file in
`~/.config/slack-send/config` and take it's settings from there. Note
that the command line options take precedence over the file config.

The tool requires a Slack webhook to be setup, you can do that from
your account settings and put the URL in your config file as
`slack.webhook_url` setting.

## Usage

```
ssend -t @yourslackusername 'your message'
ssend -t '#channelname' 'your message'
```

### ssend-notify

This is a helper tool for wrapping commands that take long time to
execute. Once the command has finished a notification will be send
with the command's status, the host it ran on, the directory it was
started in and the exit status. The wrapper can be used like this:

```
ssend-notify some long command
# or if you happen to use pipes inside
ssend-notify '(find /usr | wc -l)'
```

The arguments are just passed to `eval` of `/bin/sh`, so piped
commands need to be passed as a string.

## Installation

It is best if the tools are installed into user dir like this:

```
python setup.py install --user
```

Make sure to have `~/.local/bin` in your `$PATH`.
