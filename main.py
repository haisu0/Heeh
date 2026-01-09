# === FITUR: AI CHAT ===

async def ai_handler(event, client):
    # hanya aktif di private chat
    if not event.is_private:
        return

    me = await client.get_me()
    if event.sender_id != me.id:
        return

    # Ambil teks dari argumen
    input_text = (event.pattern_match.group(1) or "").strip()

    # Jika reply ke pesan lain
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply:
            # Jika reply adalah media (foto, video, audio, dokumen), tolak
            if reply.media:
                return

            # Ambil isi text dari reply
            if reply.message:
                if input_text:
                    input_text = f"{input_text}\n\n{reply.message.strip()}"
                else:
                    input_text = reply.message.strip()

    if not input_text:
        await event.reply("❌ Harus ada teks atau reply pesan.")
        return

    # 🔄 pesan loading keren
    loading_msg = await event.reply("🤖✨ AI sedang berpikir keras...")

    try:
        # panggil API
        url = f"https://api.siputzx.my.id/api/ai/metaai?query={input_text}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=60) as resp:
                data = await resp.json()

        if data.get("status") and "data" in data:
            output = data["data"]
        else:
            output = "⚠ AI tidak memberikan respon."

        await loading_msg.edit(f"{output}", parse_mode="markdown")

    except Exception as e:
        await loading_msg.edit(f"⚠ Error AI: `{e}`")



async def ai2_handler(event, client):
    # hanya aktif di private chat
    if not event.is_private:
        return

    me = await client.get_me()
    if event.sender_id != me.id:
        return

    # Ambil teks dari argumen
    input_text = (event.pattern_match.group(1) or "").strip()

    # Jika reply ke pesan lain
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply:
            # Jika reply adalah media (foto, video, audio, dokumen), tolak
            if reply.media:
                return

            # Ambil isi text dari reply
            if reply.message:
                if input_text:
                    input_text = f"{input_text}\n\n{reply.message.strip()}"
                else:
                    input_text = reply.message.strip()

    if not input_text:
        await event.reply("❌ Harus ada teks atau reply pesan.")
        return

    # 🔄 pesan loading keren
    loading_msg = await event.reply("🤖✨ AI sedang berpikir keras...")

    try:
        # panggil API
        url = f"https://zelapioffciall.koyeb.app/ai/castorice?text={input_text}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=60) as resp:
                data = await resp.json()

        if data.get("status") and "data" in data:
            output = data["answer"]
        else:
            output = "⚠ AI tidak memberikan respon."

        await loading_msg.edit(f"{output}", parse_mode="markdown")

    except Exception as e:
        await loading_msg.edit(f"⚠ Error AI: `{e}`")


async def ai3_handler(event, client):
    # hanya aktif di private chat
    if not event.is_private:
        return

    me = await client.get_me()
    if event.sender_id != me.id:
        return

    # Ambil teks dari argumen
    input_text = (event.pattern_match.group(1) or "").strip()

    # Jika reply ke pesan lain
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply:
            # Jika reply adalah media (foto, video, audio, dokumen), tolak
            if reply.media:
                return

            # Ambil isi text dari reply
            if reply.message:
                if input_text:
                    input_text = f"{input_text}\n\n{reply.message.strip()}"
                else:
                    input_text = reply.message.strip()

    if not input_text:
        await event.reply("❌ Harus ada teks atau reply pesan.")
        return

    # 🔄 pesan loading keren
    loading_msg = await event.reply("🤖✨ AI sedang berpikir keras...")

    try:
        # panggil API
        url = f"https://zelapioffciall.koyeb.app/ai/felo?q={input_text}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=60) as resp:
                data = await resp.json()

        if data.get("status") and "data" in data:
            output = data["result"]
            answer = output["answer"]
            
        else:
            answer = "⚠ AI tidak memberikan respon."

        await loading_msg.edit(f"{answer}", parse_mode="markdown")

    except Exception as e:
        await loading_msg.edit(f"⚠ Error AI: `{e}`")


async def ai4_handler(event, client):
    # hanya aktif di private chat
    if not event.is_private:
        return

    me = await client.get_me()
    if event.sender_id != me.id:
        return

    # Ambil teks dari argumen
    input_text = (event.pattern_match.group(1) or "").strip()

    # Jika reply ke pesan lain
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply:
            # Jika reply adalah media (foto, video, audio, dokumen), tolak
            if reply.media:
                return

            # Ambil isi text dari reply
            if reply.message:
                if input_text:
                    input_text = f"{input_text}\n\n{reply.message.strip()}"
                else:
                    input_text = reply.message.strip()

    if not input_text:
        await event.reply("❌ Harus ada teks atau reply pesan.")
        return

    # 🔄 pesan loading keren
    loading_msg = await event.reply("🤖✨ AI sedang berpikir keras...")

    try:
        # panggil API
        url = f"https://zelapioffciall.koyeb.app/ai/felo?q={input_text}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=60) as resp:
                data = await resp.json()

        if data.get("status") and "data" in data:
            output = data["result"]
            answer = output["answer"]
            
        else:
            answer = "⚠ AI tidak memberikan respon."

        await loading_msg.edit(f"{answer}", parse_mode="markdown")

    except Exception as e:
        await loading_msg.edit(f"⚠ Error AI: `{e}`")
