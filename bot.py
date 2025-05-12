import pyautogui
import os
import discord
from discord.ext import tasks
import itertools as it
import random
import sys
import requests
import re
import random
import asyncio


class DigBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

        channel = client.get_channel(1367244616402866179)
        if channel is None:
            print("Invalid channel ID.")
            return


        #198 = sa (powerhouse), 361 = cunado (patton), 569 = AB, 832 = zig
        ls_user_id = [198226746070269952, 369187271590805504, 569525803725881344, 832858137866141746]
        ls_fetch_user = [await client.fetch_user(u) for u in ls_user_id]

        NUM_REPEAT_COUNT = 3
        int_counter = 0

        while True:
            try:
                screen_img = pyautogui.screenshot(region=(2230, 1197, 5, 5)) 
                screen_img.save('test.png') # for debugging
                color2 = screen_img.getpixel((2, 2))
                print(color2)
                
                # check for yellow popup bubble
                if color2[0] >= 190 and color2[0] <= 247 and color2[1] >= 170 and color2[1] <= 200 and color2[2] >= 60 and color2[2] <= 77:
                    print('yellow bubble has popped up')

                    # if this small section is black, it is a dig. else, it can be an announcement, DM, or egg
                    screen_img2 = pyautogui.screenshot(region=(2235, 1242, 5,5))
                    screen_img2.save('test2.png') # for debugging
                    color_black = screen_img2.getpixel((2, 2))
                    print(color_black) # for debugging

                    # found a dig
                    if color_black[0] <= 40 and color_black[1] <= 40 and color_black[2] <= 40:
                        # print('real match')
                        # msg = " ".join([u.mention for u in ls_fetch_user])
                        await channel.send(f"{ls_fetch_user[0].mention} {ls_fetch_user[1].mention} {ls_fetch_user[2].mention} {ls_fetch_user[3].mention}  DIG")
                    else:
                    	await channel.send(f"possibly a dig, but likely false alarm. This message will be removed in future iterations.")


                    # how many times have we seen this popup?
                    int_counter = int_counter + 1
                    # print(int_counter)

                    # allow the process to repeat and notify user n times to allow user to distinguish from other notifications
                    if int_counter < NUM_REPEAT_COUNT:
                        next

                    # once users have been notified, click the icon, and return to world map via a series of clicks
                    else:
                        await asyncio.sleep(2)

                        # click the icon
                        pyautogui.click(x=2236, y=1233)
                        await asyncio.sleep(2)

                        # click the back arrow
                        pyautogui.click(x=1610, y=1315)
                        await asyncio.sleep(2)

                        # sometimes a second click is needed (for example if the icon was an announcement)
                        again = pyautogui.screenshot(region=(1610, 1315, 5, 5))
                        again2 = again.getpixel((2, 2))
                        
                        if again2[0] >= 241 and again2[0] <= 247 and again2[1] >= 241 and again2[1] <= 247 and again2[2] >= 241 and again2[2] <= 247:
                        	pyautogui.click(x=1610, y=1315)
                        	await asyncio.sleep(2)

                        int_counter = 0

                else:
                    print('nothing')

            # sometimes screenshot function bugs out and cause a crash. ignore and continue.
            except:
                pass

            await asyncio.sleep(5)


if __name__ == "__main__":
    client = DigBot(intents=discord.Intents.all())
    client.run("remove token")