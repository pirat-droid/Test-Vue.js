<template>
    <div>
        <select v-model="option">
            <option v-for="user in list" :value="user.id">
                {{user.attributes.username}}
            </option>
        </select>
        <mu-button @click="addUser" color="success"  align-items="end" >Add user</mu-button>
    </div>
</template>

<script>
    export default {
        name: "AddUsers",
        data(){
            return {
                option: '',
                list: ''
            }
        },
        props: {
            room: ''
        },
        created() {
            this.loadUsers()
        },
        methods:{
            //Получаю спиок пользователей
            loadUsers(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "GET",
                    success:(response) => {
                        this.list = response.data
                    }
                })
            },
            //Добавляю пользователя
            addUser(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "POST",
                    data:{
                        room: this.room,
                        user: parseInt(this.option)
                    },
                    success:(response) => {
                        alert("Add user complet")
                    },
                    error:(response) => {
                        alert("Error add user")
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
