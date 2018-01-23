import dice


async def main(message, args, client):
    print('rolling dice')
    incom = args
    incom.pop(0)
    r = "".join(incom)
    if '+' in r:
        nums = r.split('+')
        try:
            roll = dice.roll(nums[0])
            total = int(roll) + int(nums[1])
            await client.send_message(message.channel, "Rolling: " + str(roll) + " + " + str(nums[1]) + "\n Sum: " + str(total))
        except:
            await client.send_message(message.channel, "ERR: No addition value detected, remove + sign or add a number")
    elif '-' in r:
        try:
            nums = r.split('-')
            roll = dice.roll(nums[0])
            total = int(roll) - int(nums[1])
            await client.send_message(message.channel, "Rolling: " + str(roll) + " - " + str(nums[1]) + "\n Sum: " + str(total))
        except:
            await client.send_message(message.channel, "ERR: No subtraction value detected, remove - sign or add a number")
    else:
        roll = dice.roll(r)
        await client.send_message(message.channel, "Rolling: " + str(roll) + "\n Sum: " + str(int(roll)))


async def help(message, args, client):
    await client.send_message(message.channel, "To roll the dice, type !roll [number of dice]d[number of sides]+/-[number to add or subtract]")