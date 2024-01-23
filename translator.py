import discord
from discord.ext import commands
import deepl
from discord import Embed

# Define the intents your bot will use
intents = discord.Intents.default()

# Initialize the Discord bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Add your DeepL API key
deepl_api_key = "deepl-key"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_raw_reaction_add(payload):
    # Check if the reaction is added to a message
    if payload.event_type == 'REACTION_ADD':
        # Get the message
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        # Check if the reacted emoji is a flag
        flag_emoji_dict = {
            "🇺🇸": "en-us",
            "gb": "en-gb",
            "🇫🇷": "fr",
            "🇩🇪": "de",
            "🇪🇸": "es",
            "🇮🇹": "it",
            "🇵🇹": "pt",
            "🇷🇺": "ru",
            "🇦🇱": "sq",
            "🇸🇦": "ar",
            "🇧🇦": "bs",
            "🇧🇬": "bg",
            "🇨🇳": "zh-CN",
            "🇭🇷": "hr",
            "🇨🇿": "cs",
            "🇩🇰": "da",
            "🇪🇪": "et",
            "🇫🇮": "fi",
            "🇬🇷": "el",
            "🇭🇺": "hu",
            "🇮🇩": "id",
            "🇮🇳": "hi",
            "🇮🇪": "ga",
            "🇮🇸": "is",
            "🇮🇱": "he",
            "🇯🇵": "ja",
            "🇰🇷": "ko",
            "🇱🇻": "lv",
            "🇱🇹": "lt",
            "🇲🇹": "mt",
            "🇲🇪": "sr",
            "🇳🇱": "nl",
            "🇳🇴": "no",
            "🇵🇰": "ur",
            "🇵🇱": "pl",
            "🇵🇹": "pt",
            "🇷🇴": "ro",
            "🇷🇸": "sr",
            "🇸🇦": "ar",
            "🇸🇰": "sk",
            "🇸🇮": "sl",
            "🇸🇬": "sv",
            "🇹🇭": "th",
            "🇹🇷": "tr",
            "🇹🇼": "zh-TW",
            "🇺🇦": "uk",
            "🇻🇦": "la"
            # Add more flag emojis and language codes as needed
        }

        if payload.emoji.name in flag_emoji_dict:
            target_language = flag_emoji_dict[payload.emoji.name]

            try:
                # Create a DeepL translator with your API key
                translator = deepl.Translator(deepl_api_key)

                # Translate the message to the specified target language
                translation_result = translator.translate_text(message.content, target_lang=target_language)
                
                # Extract the translated text
                translated_text = translation_result.text
                
                embed_title = f'Translated to {target_language}'
                embed = Embed(title=embed_title, description=f'{translated_text}', color=0x00ff00)
                await channel.send(embed=embed)

            except Exception as e:
                await channel.send(f'An error occurred: {e}')


# Run the bot
bot.run('discord token')
