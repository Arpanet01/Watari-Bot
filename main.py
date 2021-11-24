#Versão de 17/11/2021 
#Desenvolvido por Arpanet_01, mas isso não importa. Faça o que quiser com o código. ;)

#Importações
import discord
from discord.ext import commands
from time import sleep
from discord.utils import get
import json
import asyncio


#Configurações Do Bot
prefix = '$'
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = prefix, case_insensitive = True, intents = intents)
#client.remove_command('help')

#Leitura de arquivo json
#Essencial para envio de regras.
def rules():
	with open('rules.json', 'r') as file:
		
		regras = json.load(file)
		return regras
	
#Ativação de Watari Bot
@client.event
async def on_ready():
	
	print('Watari está online')
	
	
#Entrada de Membros/Registro
@client.event
async def on_member_join(member):
	
	#Aviso: Requer criação de um arquivo json. Em determinada parte do código, o programa irá ler as regras que devem ser salvas dentro de um dicionário em um arquivo json. 
	
	global c, c2
	
	role = get(member.guild.roles, name='Novato')
	
	await member.add_roles(role)
	
	channel = client.get_channel(id) #int
	
	embed = discord.Embed(title='**Seleção de Cargos**', description='Selecione seus cargos iniciais clicando nos emojis correspondentes. 2 minutos para responder.',color= discord.Color.from_rgb(0,255,110))
	embed.add_field(name='**:computer: Programador**',value='Cargo designado a programadores em geral')
	embed.add_field(name='**:bust_in_silhouette:  Usuário**', value='Se você está aqui apenas por curiosidade, mas não tem experiência com programação, selecione esse cargo.')

	
	
	
	message = await channel.send(embed=embed, delete_after=120)
	
	cargos = []
	
	await message.add_reaction('💻')
	await message.add_reaction('👤')
	
	def check(reaction, user):
		return user == member and str(reaction.emoji) == '💻' or user == member and str(reaction.emoji) == '👤'
		
	try:
		reaction, user = await client.wait_for('reaction_add', timeout=120, check=check)
		
	except:
		
		await channel.send(f"Você não respondeu no prazo estipulado! {member.mention}", delete_after=10)
		
		add = get(member.guild.roles, name='Não Registrado')
		remove = get(member.guild.roles, name='Novato')
		await member.add_roles(add)
		await member.remove_roles(remove)
		
		return
	
	else:
		
		if str(reaction.emoji) == '💻':
			
			cargos.append("Programador")
			
		if str(reaction.emoji) == '👤':
			
			cargos.append("Usuário")
	
	
	
	embed = discord.Embed(title='**Por que se interessou pelo servidor?**',description='2 minutos para responder', color=discord.Color.from_rgb(0,255,110))
	embed.add_field(name='💡 Quero aprender com outros desenvolvedores do servidor!', value='Se seu interesse é pedir ajuda, esclarecer dúvidas, ou aprender com outros desenvolvedores, selecione esse cargo.')
	embed.add_field(name='**👥 Quero conhecer outros desenvolvedores!**', value='Se você quer se socializar, selecione essa opção.')
	embed.add_field(name='**📚 Eu quero os dois!**', value="Se você quer aprender e conhecer outras pessoas, marque essa opção.")
	
	msg = await channel.send(embed=embed, delete_after=120)
	
	await msg.add_reaction('💡')
	await msg.add_reaction('👥')
	await msg.add_reaction('📚')
	
	
	def check(reaction, user):
		
		return user == member and str(reaction.emoji) == '💡' or user == member and str(reaction.emoji) == '👥' or user == member and str(reaction.emoji) == '📚'
		
	try:
		
		reaction, user = await client.wait_for('reaction_add', timeout=120, check=check)
		
	except:
		
		await channel.send(f'Você não respondeu no prazo estipulado! {member.mention}', delete_after=10)
		add = get(member.guild.roles, name='Não Registrado')
		remove = get(member.guild.roles, name='Novato')
		await member.add_roles(add)
		await member.remove_roles(remove)
		return
	
	else:
		
		if str(reaction.emoji) == '💡':
			
			cargos.append("Aprendendo")
			
		if str(reaction.emoji) == '👥':
			
			cargos.append("Socializando")
			
		if str(reaction.emoji) == '📚':
			
			cargos.append('Aprendendo')
			cargos.append('Socializando')
	
	embed = discord.Embed(title='**Finalizar**', description='Clique em ✅ para finalizar registro. ')
	embed.set_footer(text='Obs: É necessário que permita o envio de mensagens diretas')
	
	embed_final = await channel.send(embed=embed, delete_after=120)
	
	await embed_final.add_reaction('✅')
	
	def check(reaction, user):
		
		return user == member and str(reaction.emoji) == '✅'
		
	try:
		
		reaction, user = await client.wait_for('reaction_add', timeout=120, check=check)
		
	except:
		
		await channel.send(f'Seu cadastro não foi concluído! {member.mention}',delete_after=10)
		add = get(member.guild.roles, name='Não Registrado')
		remove = get(member.guild.roles, name='Novato')
		await member.add_roles(add)
		await member.remove_roles(remove)
		return
		
		
		
	else:
	
	
		welcome = discord.Embed(title='🎉 Seja bem-vindo! 🎉',color=discord.Color.from_rgb(0,255,110))
		welcome.add_field(name='**Um pouco sobre:**', value='Seja bem-vindo ao servidor 🎉. Eu sou Watari, bot de administração desenvolvido para o servidor 🤖. Vim te dar boas-vindas e informar sobre as regras!')
	
		try:
			await member.send(embed=welcome)
		except:
			channel.send('Não foi possível enviar mensagens para sua DM. Permita o envio e reentre no servidor. ' + member.mention)
		else:
			pass
		
		embed = discord.Embed(title='Regras Do Servidor', description='Leia algumas regras do servidor! :)',color=discord.Color.from_rgb(0,255,110))
		embed.add_field(name='Regra 1', value=regras['**Regra 1**'])
		embed.set_footer(text='Use ✅ para confirmar registro.')
			
			
		msg = await member.send(embed=embed)	
		
		await msg.add_reaction('⬅️')
		await msg.add_reaction('➡️')
		await msg.add_reaction('✅')	
		
		c = 1
		c2 = 1
		while True:
			def check(reaction, user):
				
				return user == member and str(reaction.emoji) == '⬅️' or user == member and str(reaction.emoji) == '➡️' or user == member and str(reaction.emoji) == '✅'
			
			try:
				
				reaction, user = await client.wait_for('reaction_add', timeout=None, check=check)
				
			except:
				
				pass
				
			else:
				
				if str(reaction.emoji) == '➡️':
					
					c = c + 1
					c2 = c2 + 1
					
					embed = discord.Embed(title='Regras Do Servidor', description='Leia algumas regras do servidor. :)', color=discord.Color.from_rgb(0,255,110))
					
					nome = f'Regra {c2}'
					valor = f'**Regra {c}**'
					try:
						embed.add_field(name=nome, value=regras[valor])
						await msg.edit(embed=embed)			
					except Exception as erro:
						c = 1
						c2 = 1
						nome = f'Regra {c2}'
						valor = f'**Regra {c}**'
						embed.add_field(name=nome, value=regras[valor])
						embed.set_footer(text='User ✅ para confirmar registro.')
						await msg.edit(embed=embed)
					else:
						pass
					
				if str(reaction.emoji) == '⬅️':
					
					c = c - 1
					c2 = c2 - 1
					
					embed = discord.Embed(title='Regras Do Servidor', description="Leia algumas regras do servidor", color=discord.Color.from_rgb(0,255,110))
					
					nome = f'Regra {c2}'
					valor = f'**Regra {c}**'
					
					try:
						
						embed.add_field(name=nome, value=regras[valor])
						embed.set_footer(text='Use ✅ para confirmar registro.')		
						await msg.edit(embed=embed)
						
					except:
						c = len(regras) - 1
						c2 = len(regras) - 1
						nome = f'Regra {c2}'
						valor = f'**Regra {c2}**'
						embed.add_field(name=nome, value=regras[valor])
						embed.set_footer(text='Use ✅ para confirmar registro.')
						await msg.edit(embed=embed)
					else:
						pass
						
				if str(reaction.emoji) == '✅':
					cargos.append('Membro')
					for cargo in cargos:
						role = get(member.guild.roles, name=cargo)
						await member.add_roles(role)
					
					role = get(member.guild.roles, name="Novato")
					await member.add_roles(role)
					await member.remove_roles(role)
					await member.send('Registro concluído!')	
			
						
#Trancar canais
@commands.has_permissions(manage_channels=True)
@client.command()
async def lock(ctx, setting=None):
			
	if setting == None:
			
		channel = ctx.channel
		overwrite = channel.overwrites_for(ctx.guild.default_role)
		overwrite.send_messages = False
		await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
		await channel.send("Canal Fechado!")
		
	else:
		
		if str(ctx.channel.id) == 'id': #str
		
			canais_para_fechar = []
			
			if setting == 'all_channels':
				guild = ctx.guild
				
				for channel in guild.channels:
					if str(channel.type) == 'text':
						if str(channel.id) in canaisnf:
							print(f'Canal {channel.name} não pode ser fechado.')
						else:
							canais_para_fechar.append(channel)
							
				for i in canais_para_fechar:
						
					overwrite = i.overwrites_for(ctx.guild.default_role)
					overwrite.send_messages = False
					await i.set_permissions(guild.default_role, overwrite=overwrite)
					await i.send(f'Canal fechado por {ctx.author.name}')
						

					
#Enviar mensagens simultâneas para diferentes canais
@client.command()
async def tell(ctx):
	
	if str(ctx.channel.id) == 'id': #str
	
		embed = discord.Embed(title='Enviar Mensagens Simultâneas', color=discord.Color.from_rgb(0,255,110))
		embed.add_field(name='**Mandar Mensagem em Categoria Específica**', value="Se você quer mandar a mensagem em uma única categoria, marque 1️⃣")
		embed.add_field(name='**Mandar em todos os canais**', value='Se quer mandar em todos os canais, selecione 2️⃣')
		embed.set_footer(text='40 segundos para resposta')
		
		msg = await ctx.message.reply(embed=embed, mention_author=False)
		
		await msg.add_reaction('1️⃣')
		await msg.add_reaction('2️⃣')
		
		def check(reaction,user):
			
			return user == ctx.author and str(reaction.emoji) == '1️⃣' or user == ctx.author and str(reaction.emoji) == '2️⃣'
			
		try:
			
			reaction, user = await client.wait_for('reaction_add', timeout=40, check=check)
		
		except:
			
			await ctx.channel.send(f'Tempo expirado! {ctx.author.mention}')
		
		else:
			
			if str(reaction.emoji) == '1️⃣':
				
				embed = discord.Embed(title='Categorias No servidor', color=discord.Color.from_rgb(0,255,110))
				guild = ctx.guild
				c = 1
				for categorie in guild.categories:
					embed.add_field(name=f'**Categoria {c}**', value=f'{categorie.name}', inline=False)
					c = c + 1
				
				embed.add_field(name='**Escolha a categoria**', value='Escreva no chat')
				embed.set_footer(text=f'Exemplo: {guild.categories[0]}')
					
				await ctx.send(embed=embed)
				
				def check(message):
					if message.author == ctx.author and message.channel.id == ctx.channel.id:
						return check
						
				try:
					msg = await client.wait_for('message',timeout=30, check=check)
					
				except:

					await ctx.send(f'Tempo expirado! {ctx.author.mention}')
				else:
					for categories in guild.categories:
						if str(msg.content) == str(categories.name):
							category = categories
							check = 'sim'
							break
						else:
							check = 'não'
					
										
												
					if check == 'sim':
						
						embed = discord.Embed(title='Mensagem que será enviada', description='Escreva a mensagem que sera enviada para todos da categoria selecionada.', color=discord.Color.from_rgb(0,255,110))
						embed.set_footer(text='60 segundos para responder.')
						
						await msg.reply(embed=embed, mention_author=False)
						
						def check(message):
							if message.author == ctx.author and message.channel.id == ctx.channel.id:
								return check
								
						try:
							msg = await client.wait_for('message',timeout=60,check=check)
						except:
							await ctx.send(f'Tempo expirado! {ctx.author.mention}')
						else:
							for channel in category.channels:
								if str(channel.type) == 'text':
									embed = discord.Embed(title='Mensagem Global', description=f'{ctx.author.name} enviou uma mensagem para todos os canais dessa categoria.')
									embed.add_field(name='Conteúdo Da Mensagem', value=f'{msg.content}')
								
									await channel.send(embed=embed)
					
					else:
						await ctx.send(f'A categoria especificada não foi encontrada. {ctx.author.mention}')
						return					
			
			if str(reaction.emoji) == '2️⃣':
				embed = discord.Embed(title='Mensagem que será enviada', description='Escreva a mensagem que sera enviada para todos os canais do servidor.', color=discord.Color.from_rgb(0,255,110))
				embed.set_footer(text='60 segundos para responder.')
						
				await msg.reply(embed=embed, mention_author=False)
						
				def check(message):
					if message.author == ctx.author and message.channel.id == ctx.channel.id:
						return check
								
				try:
					msg = await client.wait_for('message',timeout=60,check=check)
				except:
					await ctx.send(f'Tempo expirado! {ctx.author.mention}')
				else:
					guild = ctx.guild
					for channel in guild.channels:
						if str(channel.type) == 'text':
							embed = discord.Embed(title='Mensagem Global', description=f'{ctx.author.name} enviou uma mensagem para todos os canais do servidor.')
							embed.add_field(name='Conteúdo Da Mensagem', value=f'{msg.content}')
								
							await channel.send(embed=embed)
				

					
					
#Destrancar canais
@commands.has_permissions(manage_channels=True)
@client.command()
async def unlock(ctx, setting=None):
	

	
	if setting == None:
		channel = ctx.channel
		overwrite = channel.overwrites_for(ctx.guild.default_role)
		overwrite.send_messages = True
		await channel.set_permissions(ctx.guild.default_role,overwrite=overwrite)
		await channel.send('Canal Aberto!')				
	else:
		
		if str(ctx.channel.id) == 'id': #str
			if setting == 'all_channels':
				canais_para_fechar = []
				
				guild = ctx.guild
				
				for channel in guild.channels:
					if str(channel.type) == 'text':
						if str(channel.id) in canaisnf:
							print(f'Canal {channel.name} não pode ser fechado.')
						else:
							canais_para_fechar.append(channel)
				
				for i in canais_para_fechar:
					overwrite = i.overwrites_for(ctx.guild.default_role)
					overwrite.send_messages = True
					await i.set_permissions(guild.default_role, overwrite=overwrite)
					await i.send(f'Canal aberto por {ctx.author.name}')
						
		
		


#Envio de regras
@client.command()
async def rules(ctx):
	global embed_msg
	
	canal = client.get_channel()

	if str(ctx.author.id) == 'id': #str
		
				
		embed = discord.Embed(title='📜 Regras Do Servidor', descrition="Leia aqui as regras do servidor",	color= discord.Color.from_rgb(0,255,110))
	
		for i in regras:
			
			embed.add_field(name=i, value=regras[i], inline=False)
	
		embed_msg = await canal.send(embed=embed)
		



#Informações sobre o bot
@client.command()
async def watari(ctx):
	
	if ctx.channel.id == id: #int
	
		embed = discord.Embed(title='Informações sobre Watari', color=discord.Color.from_rgb(0,255,110))
		embed.add_field(name='**Quem sou eu?**', value='Sou um bot desenvolvido para esse servidor. Meu objetivo é ajudar na administração. Fui desenvolvido por: **Arpanet_01**.', inline=False)
		embed.add_field(name='Linguagens usadas:', value='🐍 Python',inline=False)
		
		await ctx.send(embed=embed)
		
	else:
		
		await ctx.message.reply('Canal incorreto! ', mention_author=False)

		
				
		
#Informações sobre um usuário
@client.command()
async def whois(ctx, member: discord.Member = None):
	
	if member == None:
		member = ctx.author

	
	if ctx.channel.id == id: #int
		date_format = "%a, %d %b %Y %I:%M %p"
		
		embed = discord.Embed(title=f'Informações sobre **{member.name}**', color=discord.Color.from_rgb(0,255,110))
		embed.set_author(name=str(member), icon_url=member.avatar_url)
		embed.add_field(name='**Nome De Usuário:**', value=member.name,inline=True)
		embed.add_field(name='**Apelido:**', value=member.nick, inline=True)
		embed.add_field(name='**Entrou em:**', value=member.joined_at.strftime(date_format), inline=False)
		embed.add_field(name='**Conta criada em:**', value=member.created_at.strftime(date_format), inline=True)
		
		embed.set_footer(text=f'ID: {member.id}')
		
		
		await ctx.message.reply(embed=embed, mention_author=False)
	
	else:
		await ctx.message.reply('Canal incorreto!', mention_author=False)
		

#Avatar de um usuário
@client.command()
async def avatar(ctx, member: discord.Member = None):
	
	if str(ctx.channel.id) == 'id': #str 
	
		if member == None:
			member = ctx.author
			
		embed = discord.Embed(title=f"Avatar de {member.name}", url=f'{member.avatar_url}', color=discord.Color.from_rgb(0,255,110))
		embed.set_image(url=member.avatar_url)
		
		await ctx.message.reply(embed=embed, mention_author=False)
	
	else:
		
		await ctx.message.reply('Canal incorreto!', mention_author=False)
	
	
#Banir usuário	
@client.command()
async def ban(ctx, member=None):
	
	
	if member == None:
		return
	
	guild = ctx.guild
	
	member = guild.get_member(int(member))  
	
	if str(ctx.channel.id) == 'id': #str
		
		embed = discord.Embed(title='Motivo do Banimento', description="Qual é o motivo para esse banimento?")
		embed.set_footer(text='Envie no chat')
		
		await ctx.message.reply(embed=embed, mention_author=False)
		
		def check(message):
			if message.author == ctx.author and message.channel.id == ctx.channel.id:
				return check
				
		
		
		try:
		
			msg = await client.wait_for('message', timeout=60, check=check)
			
		except:
			
			await ctx.channel.send('Tempo expirado! ' + ctx.author.mention)
			return
		
		else:
			
			motivo = msg.content
		
		
		embed = discord.Embed(title='Confirmar Banimento',description=f'Tem certeza de que quer banir o usuário {member.name}? Pense bem antes de confirmar.', color=discord.Color.from_rgb(0,255,110))
		
		mensagem = await ctx.message.reply(embed=embed,mention_author=False)
		
		await mensagem.add_reaction('✅')
		
		def check(reaction,user):
			
			return user == ctx.author and str(reaction.emoji) == '✅'
			
		try:
			
			reaction, user = await client.wait_for('reaction_add', timeout=30, check=check)
			
		except:
			
			await ctx.channel.send('Tempo de resposta expirado! ' + ctx.author.mention)
			return
			
		else:
			
			m = member
			nomeb=member.name
			
			embed = discord.Embed(title='Você foi banido do servidor', color=discord.Color.from_rgb(0,255,110))
			embed.add_field(name='**Administrador responsável pelo banimento:**', value=f'{ctx.author.name}')
			embed.add_field(name='**Motivo: **', value=f'{motivo}')
			embed.set_footer(text='Acha que seu ban não foi merecido? Tente contatar alguns administradores do servidor. :)')
			
			try:
				await m.send(embed=embed)
			except:
				print('Não foi possível enviar mensagens diretas para esse usuário')
			else:
				pass
			
			
			await ctx.guild.ban(member)		
			await ctx.message.reply(f"Usuário {member.name} foi banido.")
			
			embed = discord.Embed(title="Registro De Banimento", color=discord.Color.from_rgb(0,255,110))
			embed.add_field(name="**Banido por:**", value=f'{ctx.author.name}')
			embed.add_field(name='**Usuário banido:**',value=f'{nomeb}')
			embed.add_field(name='**Motivo:** ', value=f'{motivo}')
			embed.set_image(url='https://c.tenor.com/HLx4m-urlBEAAAAM/kick-anime.gif')
			
			channel = client.get_channel(id) #int
			
			
			
			await channel.send(embed=embed)
			
			
			

#Deter usuário
@client.command()
async def deter(ctx, id = None):
		
		channel = ctx.channel
		guild = ctx.guild
		
					
		if id == None:
			await ctx.message.reply("Especifique um ID!", mention_author=False)
			return
		

		if ctx.channel.id == #id do canal:
			iddeter = guild.get_member(int(id))
			if hasattr(iddeter, 'name'):
				embed = discord.Embed(title='Formulário de Punição', description="Preencha o formulário", color=discord.Color.from_rgb(0,255,110))
				embed.add_field(name='**Digite o motivo da punição**', value='Antes de deter um usuário, esclareça o motivo. Envie o motivo no chat.')
				
				await ctx.message.reply(embed=embed, mention_author=False)
				def check(m):
					
					if m.author == ctx.author and m.channel.id == channel.id:
						return check
				
				
				try:	
					msg = await client.wait_for('message', check=check, timeout=60)
				except:
					await ctx.message.reply("Tempo de resposta expirado!",mention_author=False)
					return
				else:
					motivo = msg.content
					embed = discord.Embed(title="Confirmar punição",description="Confirme a punição", color=discord.Color.from_rgb(0,255,110))
					embed.add_field(name='**Punir usário:**', value=f'{iddeter.name}')
					embed.add_field(name='**Motivo:**', value=f'{motivo}' or 'Não especificado', inline=True)
					embed.set_footer(text="Clique em ✅ para confirmar punição.")
					
					message = await msg.reply(embed=embed)
					await message.add_reaction('✅')
					
					def check(reaction,user):
						
						return user == ctx.author and str(reaction.emoji) == '✅'
						
					try:
					
						reaction, user = await client.wait_for('reaction_add', timeout=30, check=check)
					
					except:
						
						await ctx.send('Tempo expirado!' + ctx.author.mention)
					
					else:
						
						for role in iddeter.roles:
							if str(role) == '@everyone':
								pass
							else:
								role = get(guild.roles, name=str(role))
								await iddeter.remove_roles(role)
						
						role = get(guild.roles, name='Detento')
						await iddeter.add_roles(role)
						
						await ctx.send("Usuário detido! ", ctx.author.mention)
						
						channel = client.get_channel(id) #int
						
						embed = discord.Embed(title='Log de Punição', description='Informações sobre punição',color=discord.Color.from_rgb(0,255,110))
						embed.add_field(name='**Aplicada por:**', value=f'{ctx.author.name}')
						embed.add_field(name='**Usuário detido:**', value=f'{iddeter.name}', inline=False)
						embed.add_field(name='**Motivo:**', value=f'{motivo}')
						embed.set_image(url='https://pa1.narvii.com/6449/94943f6140a73df4b245a72749f0c2b431b79af4_hq.gif')
						
						await channel.send(embed=embed)
						
						channel = client.get_channel(id) #int
						
						embed = discord.Embed(title='Você foi detido!',description=f'Você foi detido por {ctx.author.name}. {iddeter.mention}', color=discord.Color.from_rgb(0,255,110))
						embed.add_field(name='**Motivo da punição:**', value=f"{motivo}")
						embed.set_footer(text='Aguarde até que seja solto.')
						
						await channel.send(embed=embed)
						
					
		else:
			await ctx.message.reply("ID inválido.", mention_author=False)
			
					
	
client.run('token')
