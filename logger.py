import datetime

# Today's date in formatted string
date = datetime.date.today().strftime("%d %B, %Y - %A")

# Taking input
progress = input('Today\'s Progress = ')
thoughts = input('Thoughts = ')
links = input('Links (comma separated) = ')

# Getting the current day
dayf = open('day.int', 'r')
day = int(dayf.read())
dayf.close()

# Creating log entry
log = '### Day ' + str(day) + ': ' + date + '\n'
log = log + '**Today\'s Progress:** ' + progress + '\n\n'
log = log + '**Thoughts:** ' + thoughts + '\n\n'
log = log + '**Link(s):** '

# TODO: Check for no links
links = links.split(',')
for link in links:
    link = link.split('-')
    # TODO: Check for no title
    log = log + '[' + link[0] + '](' + link[1] + ')\n'
log = log + '\n\n'

# Updating the day value
dayf = open('day.int', 'w')
dayf.write(str(day + 1))
dayf.close()

# Writing to log file
f = open('log.md', 'a')
f.write(log)
f.close()
