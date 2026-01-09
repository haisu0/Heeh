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




# ===== FITUR CONFESS =====
import asyncio, random, string
from telethon import events

# State global, dipisahkan per akun (client)
confess_sessions = {}    # {client_id: {user_id: True}}
pending_confess = {}     # {client_id: {msg_id: {"sender": id, "target": id}}}
rooms = {}               # {client_id: {room_id: {"sender": id, "target": id, "messages": [], "expire": task}}}

def gen_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def _init_client_state(client):
    cid = id(client)
    confess_sessions.setdefault(cid, {})
    pending_confess.setdefault(cid, {})
    rooms.setdefault(cid, {})
    return cid

def _user_in_active_room(cid, user_id):
    for rid, room in rooms[cid].items():
        if user_id in (room["sender"], room["target"]):
            return rid
    return None

def _user_has_pending_confess(cid, user_id):
    for mid, data in pending_confess[cid].items():
        if data.get("sender") == user_id or data.get("target") == user_id:
            return True
    return False

async def confess_handler(event, client):
    if not event.is_private:
        return  # hanya aktif di private chat

    text = (event.message.message or "").strip()
    sender_id = event.sender_id
    cid = _init_client_state(client)

    # === /cancel: batalkan sesi pengisian format ===
    if text == "/cancel":
        if confess_sessions[cid].pop(sender_id, None):
            await event.reply("✅ Sesi confess dibatalkan.")
        else:
            await event.reply("ℹ️ Tidak ada sesi confess yang aktif.")
        return

    # === /confess: mulai sesi, blokir jika user sedang aktif/pending ===
    if text == "/confess":
        if _user_in_active_room(cid, sender_id):
            await event.reply("❌ Kamu masih berada di room anonim yang aktif. Selesaikan dulu dengan `/endchat`.")
            return
        if
