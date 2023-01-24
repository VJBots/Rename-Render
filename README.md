### Give a star and Fork the Repo or You can Use this as a Template also.

####  Features
 - Renames very fast .
 - Permanent Thumbnail support.
 - Supports Broadcasts.
 - Set custom caption.
 - Has a custom Start-up pic.
 - Force subscribe available.
 - Supports unlimited renaming at a time.
 - Developer Service 24x7. 🔥

 ###  Configs 

* `BOT_TOKEN`  - Get bot token from @BotFather
* `API_ID` - From my.telegram.org 
* `API_HASH` - From my.telegram.org 
* `ADMIN` - AUTH or bot controllers id's multiple id use space to split 
* `FORCE_SUB` - Force Subscribe Channel name without@. Enable only if you need strict mode.
* `DB_URL`  - Mongo Database URL from https://cloud.mongodb.com/
* `DB_NAME`  - Your database name from mongoDB.


### Deploy on VPS

 * Clone the Repo.

```
git clone https://github.com/WebX-Divin/Rename-Bot-V1.0
```
 * Move to the Repo Folder in the VPS.

```
cd Rename-Bot-V1.0
```
 * Inside the cloned folder edit config.py and install the pip, by the following command.

```
apt install python3-pip
```

 * Make sure you update your directory once you installed pip
 ```
 apt update && upgrade
 ```
 
 * Install the required modules using the following command.

```
pip install -r requirements.txt
```

 * If you want to run the bot 24x7, then use this command to create a nested virtual environment.

```
sudo apt install tmux
```

```
tmux
```
* If you don't use tmux, then you can directly use this command after the requirements.txt is installed in your VPS.
 
```
python3 bot.py
```

### Deploy on Render
 - Star and click on the Use this Template Button.
 - Set Your Repo as Private.
 - Add your Environmental Variables in the config.py file.
 - Go to Render and Create a new web service and turn of Auto Deploy.
 - Then scroll down and click on the 'Create Web Service' Button.
 - That's it. You're Done.


###  Commands
`/start` - Check if the bot is running.

`/viewthumb` - To view current thumbnail.

`/delthumb` - To delete current thumbnail.

`/set_caption` - set a custom caption.

`/see_caption` - see your custom caption.

`/del_caption` - delete custom caption.

`/users` - To view list of users, using BOT [FOR ADMINS USE ONLY]

`/broadcast` - Message Broadcast command [FOR ADMINS USE ONLY].


#### Join Telegram Channel 
 - [WebXBots](https://t.me/WebXBots). Bot Updates Channel
 - Support Group [WebX-Support](https://t.me/Web_X_Support). For Bug report.
