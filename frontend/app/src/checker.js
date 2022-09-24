import {login_state} from "./stores";
import {toast} from "@zerodevx/svelte-toast";
import {navigate} from "svelte-routing";
import {onMount} from "svelte";

let logged;

export async function check_key(key){
        fetch('http://127.0.0.1:8000/check/'+key)
        .then((response) => response.json())
        .then((res) => {
			res = res[0].toLowerCase()
            login_state.set(eval(res))
            login_state.subscribe((value) => logged = value)
            if(logged) {
				toast.push("key is "+  res, {
			  		theme: {
						'--toastBackground': '#3a9463',
						'--toastBarBackground': '#246545',
			  		},
					duration: 1800
				})
			} else {
  				toast.push("key is "+  res, {
  					theme: {
						'--toastBackground': '#cc4040',
						'--toastBarBackground': '#752424'
  					},
					duration: 1800
				})
			}
        })
    }