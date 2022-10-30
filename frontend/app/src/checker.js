import {board_name_wt, login_state_wt, server_url} from "./stores";
import {toast} from "@zerodevx/svelte-toast";
import {navigate} from "svelte-routing";
import {onMount} from "svelte";

let logged;

let url = '';

server_url.subscribe(value => {
        url = value
})

export async function check_key(key){
        fetch(url + 'check/'+key)
        .then((response) => response.json())
        .then((res) => {
            login_state_wt.set(eval(res['state']))
            login_state_wt.subscribe((value) => logged = value)
            if(logged) {
				board_name_wt.set(res['name'])
				/*
				toast.push("key is valid", {
			  		theme: {
						'--toastBackground': '#3a9463',
						'--toastBarBackground': '#246545',
			  		},
					duration: 1800
				})
				 */
			} else {
  				toast.push("key not valid ", {
  					theme: {
						'--toastBackground': '#cc4040',
						'--toastBarBackground': '#752424'
  					},
					duration: 1800
				})
			}
        })
    }