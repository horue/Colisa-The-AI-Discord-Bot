import discord
from discord.ext import commands

helpe = discord.Embed(
    title = "Needing some help? Let's go!",
    description = 'Here you can find an overview of what I can do.\n For now, I am still at the start of my developtment, but the AI features of conversation are working.',
    color = 15410105
  )

helpe.set_author(name= f'Colisa Bot Help Screen', icon_url= 'https://www.tibiawiki.com.br/images/d/d7/Golden_Newspaper.gif')

helpe.set_thumbnail(url = 'https://www.tibiawiki.com.br/images/d/d7/Golden_Newspaper.gif')

helpe.set_image(url= 'https://64.media.tumblr.com/554afaca94ce64ce2f1943e373dee212/69093404c1702635-ad/s640x960/5a1c90b56d1e1386234f548c2920c6b4eca80f62.jpg')

helpe.set_footer(text= f'Bot developed by horue. Gemini AI developed by Google.')

helpe.add_field(name= 'About Colisa AI Bot', value= "Colisa is a powerful discord bot powered with Google's Gemini AI! That enables you to ask her anything you want!", inline=False)
helpe.add_field(name= 'How can I use this AI assistant?', value= '•** Ask questions:** Type in your question and hit enter.\n•** Provide context:** If needed, provide additional information to help the assistant understand your question.\n•** Be specific:** The more specific your question, the better the assistant can help you.', inline=False)
helpe.add_field(name= 'Need more help?', value= "If you want more info about what I can do, check out my dev's GitHub: https://github.com/horue/Colisa-The-AI-Discord-Bot", inline=False)
helpe.add_field(name= 'Additional Information', value= "If, for some reason, Google Gemini is offline or unable to answer any question, the generated text will be provide via Ollama, using Mistral model.", inline=False)


