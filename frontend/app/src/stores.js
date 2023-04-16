import { writable } from 'svelte/store';

export const login_state_wt = writable(0);
export const key_wt = writable("")
export const board_name_wt = writable("")
export const server_url = writable("https://api.syncave.com/")
//  export const server_url = writable("http://127.0.0.1:8000/")