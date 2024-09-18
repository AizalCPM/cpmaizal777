import random
import requests
from time import sleep
import os
import signal
import sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate
from cpmewan import CPMEwan
__CHANNEL_USERNAME__ = 'Ewan1999Ewan'
__GROUP_USERNAME__ = 'Ewan19_99Ewan'

def signal_handler(sig, frame):
    print('\n Bye Bye...')
    sys.exit(0)


def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                if width > 1:
                    pass
                if height > 1:
                    pass
                color_index = (width - 1) / 1((y + (height - 1) / 1) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)
                style = Style(color = colors[color_index])
                colorful_text.append(char, style = style)
            colorful_text.append(char)
            colorful_text.append('\n')
            return colorful_text


def banner(console):
    if os.name == 'nt':
        pass
    'cls'('clear')
    brand_name = 'ââââââ   ââââââ   ââââ âââââââââââ  â     ââ âââ       ââââ    â \n'
    brand_name += 'ââââ ââ  ââââ  ââââââââââ âââââ   â âââ â âââââââââ     ââ ââ   â \n'
    brand_name += 'âââ    â ââââ âââââââ    ââââââââ   âââ â ââ âââ  âââ  âââ  ââ âââ\n'
    brand_name += 'ââââ âââââââââââ ââââ    âââ âââ  â âââ â ââ âââââââââ ââââ  âââââ\n'
    brand_name += 'â âââââ âââââ â  âââââ   âââââââââââââââââââ  ââ   ââââââââ   ââââ\n'
    brand_name += 'â ââ â  âââââ â  ââ ââ   â  âââ ââ ââ âââ â   ââ   âââââ ââ   â â \n'
    colors = [
        'rgb(255,0,0)',
        'rgb(255,69,0)',
        'rgb(255,140,0)',
        'rgb(255,215,0)',
        'rgb(173,255,47)',
        'rgb(0,255,0)',
        'rgb(0,255,255)',
        'rgb(0,191,255)',
        'rgb(0,0,255)',
        'rgb(139,0,255)',
        'rgb(255,0,255)']
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         ðððððð ðððððð ðððð ððð ðððððð ððððð ðððð ðððð'))
    print(Colorate.Horizontal(Colors.rainbow, '    ððððððð ððð ðððððð ððð ðð ððð ððððððð ððð ðððð ðð ððððððð'))
    print(Colorate.Horizontal(Colors.rainbow, f''' â           ððð¥ðð ð«ðð¦: @{__CHANNEL_USERNAME__} ðð« @{__GROUP_USERNAME__}'''))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))


def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
            print(Colorate.Horizontal(Colors.rainbow, '==========[ PLAYER DETAILS ]=========='))
            if 'Name' in data:
                pass
            Colorate.Horizontal(Colors.rainbow('Name   : ', f'''{'UNDEFINED'}.'''))
            print(Colorate.Horizontal(Colors.rainbow, f'''LocalID: {data.get('localID')}.'''))
            print(Colorate.Horizontal(Colors.rainbow, f'''Money  : {data.get('money')}.'''))
            print(Colorate.Horizontal(Colors.rainbow, f'''Coins  : {data.get('coin')}.'''))
            return None
        None(Colorate.Horizontal(Colors.rainbow, '! ERROR: new accounts most be signed-in to the game at least once !.'))
        exit(1)
        return None
    None(Colorate.Horizontal(Colors.rainbow, '! ERROR: seems like your login is not properly set !.'))
    exit(1)


def load_key_data(cpm):
    data = cpm.get_key_data()
    print(Colorate.Horizontal(Colors.rainbow, '========[ ACCESS KEY DETAILS ]========'))
    print(Colorate.Horizontal(Colors.rainbow, f'''Access Key : {data.get('access_key')}.'''))
    print(Colorate.Horizontal(Colors.rainbow, f'''Telegram ID: {data.get('telegram_id')}.'''))
    if not data.get('is_unlimited'):
        pass
    Colorate.Horizontal(Colors.rainbow('Balance $  : ', f'''{'Unlimited'}.'''))


def prompt_valid_value(content, tag, password = (False,)):
    value = Prompt.ask(content, password = password)
    if value or value.isspace():
        print(Colorate.Horizontal(Colors.rainbow, f'''{tag} cannot be empty or just spaces. Please try again.'''))
    return value


def load_client_details():
    response = requests.get('http://ip-api.com/json')
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '=============[ ðððððððð ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'''Ip Address : {data.get('query')}.'''))
    print(Colorate.Horizontal(Colors.rainbow, f'''Location   : {data.get('city')} {data.get('regionName')} {data.get('countryCode')}.'''))
    print(Colorate.Horizontal(Colors.rainbow, f'''Country    : {data.get('country')} {data.get('zip')}.'''))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ ðððð ]==============='))


def interpolate_color(start_color, end_color, fraction):
int(start_color[i:i + 2], 16)None)((1, 3, 5)())
int(end_color[i:i + 2], 16)None)((1, 3, 5)())
    interpolated_rgb = (lambda .0 = None: for start, end in .0:
int(start + fraction * (end - start))None)(zip(start_rgb, end_rgb)())
    return interpolated_rgb


def rainbow_gradient_string(customer_name):
    modified_string = ''
    num_chars = len(customer_name)
    start_color = '{:06x}'.format(random.randint(0, 16777215))
    end_color = '{:06x}'.format(random.randint(0, 16777215))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'''[{interpolated_color}]{char}'''
        return modified_string

if __name__ == '__main__':
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    banner(console)
    acc_email = prompt_valid_value('[bold][?] Account Email[/bold]', 'Email', password = False)
    acc_password = prompt_valid_value('[bold][?] Account Password[/bold]', 'Password', password = False)
    acc_access_key = prompt_valid_value('[bold][?] Access Key[/bold]', 'Access Key', password = False)
    console.print('[bold cyan][%] Trying to Login[/bold cyan]: ', end = None)
    cpm = CPMEwan(acc_access_key)
    login_response = cpm.login(acc_email, acc_password)
    if login_response != 0:
        if login_response == 100:
            print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND.'))
            sleep(2)
        if login_response == 101:
            print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD.'))
            sleep(2)
        if login_response == 103:
            print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN.'))
        print(Colorate.Horizontal(Colors.rainbow, '! Note: make sure you filled out the fields !.'))
        sleep(2)
    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL.'))
    sleep(2)
    banner(console)
    load_player_data(cpm)
    load_key_data(cpm)
    load_client_details()
    choices = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22']
    print(Colorate.Horizontal(Colors.rainbow, '{01}: Increase Money           1.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{02}: Increase Coins           3.500K'))
    print(Colorate.Horizontal(Colors.rainbow, '{03}: King Rank                4.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{04}: Change ID                3.500K'))
    print(Colorate.Horizontal(Colors.rainbow, '{05}: Change Name              1.00'))
    print(Colorate.Horizontal(Colors.rainbow, '{06}: Change Name (Rainbow)    1.00'))
    print(Colorate.Horizontal(Colors.rainbow, '{07}: Number Plates            2.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{08}: Account Delete           FREE'))
    print(Colorate.Horizontal(Colors.rainbow, '{09}: ccount Register          FREE'))
    print(Colorate.Horizontal(Colors.rainbow, '{10}: Delete Friends           5.00'))
    print(Colorate.Horizontal(Colors.rainbow, '{11}: Unlock Paid Cars         4.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{12}: Unlock all Cars          3.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{13}: Unlock all Cars Siren    2.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{14}: Unlock w16 Engine        3.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{15}: Unlock All Horns         3.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{16}: Unlock Disable Damage    2.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{17}: Unlock Unlimited Fuel    2.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{18}: Unlock House 3           3.500K'))
    print(Colorate.Horizontal(Colors.rainbow, '{19}: Unlock Smoke             2.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{20}: Change Race Wins         1.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{21}: Change Race Loses        1.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{22}: Clone Account            5.000K'))
    print(Colorate.Horizontal(Colors.rainbow, '{0} : Exit'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ ðððâ ]==============='))
    service = IntPrompt.ask(f'''[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]''', choices = choices, show_choices = False)
    print(Colorate.Horizontal(Colors.rainbow, '===============[ ðððâ ]==============='))
    if service == 0:
        print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}.'''))
    if service == 1:
        print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much money do you want.'))
        amount = IntPrompt.ask('[?] Amount')
        console.print('[%] Saving your data: ', end = None)
        if amount > 0 and amount <= 999999999:
            if cpm.set_player_money(amount):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                    'y',
                    'n'], default = 'n')
                if answ == 'y':
                    print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
        sleep(2)
    if service == 2:
        print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much coins do you want.'))
        amount = IntPrompt.ask('[?] Amount')
        console.print('[%] Saving your data: ', end = None)
        if amount > 0 and amount <= 999999999:
            if cpm.set_player_coins(amount):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                    'y',
                    'n'], default = 'n')
                if answ == 'y':
                    print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
        sleep(2)
    if service == 3:
        console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end = None)
        console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end = None)
        sleep(2)
        console.print('[%] Giving you a King Rank: ', end = None)
        if cpm.set_player_rank():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 4:
        print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new ID.'))
        new_id = Prompt.ask('[?] ID')
        console.print('[%] Saving your data: ', end = None)
        if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
            if cpm.set_player_localid(new_id.upper()):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                    'y',
                    'n'], default = 'n')
                if answ == 'y':
                    print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please use valid ID.'))
        sleep(2)
    if service == 5:
        print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Name.'))
        new_name = Prompt.ask('[?] Name')
        console.print('[%] Saving your data: ', end = None)
        if len(new_name) >= 0 and len(new_name) <= 999999999:
            if cpm.set_player_name(new_name):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                    'y',
                    'n'], default = 'n')
                if answ == 'y':
                    print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
        sleep(2)
    if service == 6:
        print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Rainbow Name.'))
        new_name = Prompt.ask('[?] Name')
        console.print('[%] Saving your data: ', end = None)
        if len(new_name) >= 0 and len(new_name) <= 999999999:
            if cpm.set_player_name(rainbow_gradient_string(new_name)):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                    'y',
                    'n'], default = 'n')
                if answ == 'y':
                    print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
        sleep(2)
    if service == 7:
        console.print('[%] Giving you a Number Plates: ', end = None)
        if cpm.set_player_plates():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 8:
        print(Colorate.Horizontal(Colors.rainbow, '[!] After deleting your account there is no going back !!.'))
        answ = Prompt.ask('[?] Do You want to Delete this Account ?!', choices = [
            'y',
            'n'], default = 'n')
        if answ == 'y':
            cpm.delete()
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
    if service == 9:
        print(Colorate.Horizontal(Colors.rainbow, '[!] Registring new Account.'))
        acc2_email = prompt_valid_value('[?] Account Email', 'Email', password = False)
        acc2_password = prompt_valid_value('[?] Account Password', 'Password', password = False)
        console.print('[%] Creating new Account: ', end = None)
        status = cpm.register(acc2_email, acc2_password)
        if status == 0:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            print(Colorate.Horizontal(Colors.rainbow, 'INFO: In order to tweak this account with CPMEwan.'))
            print(Colorate.Horizontal(Colors.rainbow, 'you most sign-in to the game using this account.'))
            sleep(2)
        if status == 105:
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, 'This email is already exists !.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 10:
        console.print('[%] Deleting your Friends: ', end = None)
        if cpm.delete_player_friends():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 11:
        console.print("[!] Note: this function takes a while to complete, please don't cancel.", end = None)
        console.print('[%] Unlocking All Paid Cars: ', end = None)
        if cpm.unlock_paid_cars():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 12:
        console.print('[%] Unlocking All Cars: ', end = None)
        if cpm.unlock_all_cars():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 13:
        console.print('[%] Unlocking All Cars Siren: ', end = None)
        if cpm.unlock_all_cars_siren():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 14:
        console.print('[%] Unlocking w16 Engine: ', end = None)
        if cpm.unlock_w16():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 15:
        console.print('[%] Unlocking All Horns: ', end = None)
        if cpm.unlock_horns():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 16:
        console.print('[%] Unlocking Disable Damage: ', end = None)
        if cpm.disable_engine_damage():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 17:
        console.print('[%] Unlocking Unlimited Fuel: ', end = None)
        if cpm.unlimited_fuel():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 18:
        console.print('[%] Unlocking House 3: ', end = None)
        if cpm.unlock_houses():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 19:
        console.print('[%] Unlocking Smoke: ', end = None)
        if cpm.unlock_smoke():
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
        sleep(2)
    if service == 20:
        print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you win.'))
        amount = IntPrompt.ask('[?] Amount')
        console.print('[%] Changing your data: ', end = None)
        if amount > 0 and amount <= 0x33B2E3C9FD0803CE7FFFFFFL:
            if cpm.set_player_wins(amount):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                    'y',
                    'n'], default = 'n')
                if answ == 'y':
                    print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
        sleep(2)
    if service == 21:
        print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you lose.'))
        amount = IntPrompt.ask('[?] Amount')
        console.print('[%] Changing your data: ', end = None)
        if amount > 0 and amount <= 0x3635C9ADC5DE9FFFFFL:
            if cpm.set_player_loses(amount):
                print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                    'y',
                    'n'], default = 'n')
                if answ == 'y':
                    print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
            print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
            print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
            sleep(2)
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
        sleep(2)
    if service == 22:
        print(Colorate.Horizontal(Colors.rainbow, '[!] Please Enter Account Detalis.'))
        to_email = prompt_valid_value('[?] Account Email', 'Email', password = False)
        to_password = prompt_valid_value('[?] Account Password', 'Password', password = False)
        console.print('[%] Cloning your account: ', end = None)
        if cpm.account_clone(to_email, to_password):
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
            print(Colorate.Horizontal(Colors.rainbow, '======================================'))
            answ = Prompt.ask('[?] Do You want to Exit ?', choices = [
                'y',
                'n'], default = 'n')
            if answ == 'y':
                print(Colorate.Horizontal(Colors.rainbow, f'''Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'''))
        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
        print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
        sleep(2)
    return None
