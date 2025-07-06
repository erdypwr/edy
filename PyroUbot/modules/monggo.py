# monggo.py
# Database helper for spamg2.py

from PyroUbot.core.database.variabel import get_list_from_vars, add_to_vars, remove_from_vars

# Synchronous wrappers for async DB functions (for compatibility with spamg2.py)
import asyncio

def ambil_spdb(user_id):
    # Returns list of chat_ids from DB_ID for the user
    return asyncio.get_event_loop().run_until_complete(get_list_from_vars(user_id, "DB_ID"))

def tambah_spdb(user_id, chat_id):
    return asyncio.get_event_loop().run_until_complete(add_to_vars(user_id, "DB_ID", chat_id))

def kureng_spdb(user_id, chat_id):
    return asyncio.get_event_loop().run_until_complete(remove_from_vars(user_id, "DB_ID", chat_id))
