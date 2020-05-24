<template>
    <div span="4" sm="4" class="room-list">
        <mu-button @click="addRoom" color="success"  align-items="end" >Add room</mu-button>
        <div v-for="room in rooms" class="one-room">
            <mu-container>
                <h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
                <small>{{room.date}}</small>
            </mu-container>
        </div>

    </div>
</template>

<script>
    // import $ from 'jquery'

    export default {
        name: "Room",
        data(){
            return{
                rooms: ''
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.LoadRoom()
        },
        methods: {
            LoadRoom(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id) {
                this.$emit("OpenDialog", id)
            },
            //Добавление комнаты
            addRoom(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "POST",
                    success: (response) => {
                        this.LoadRoom()
                    },
                    error:(response) => {
                        alert(response.statusText)
                    }
                })
            }
        },

    }
</script>

<style scoped>
    h3{
        cursor: pointer;
    }

    .room-list{
        margin: 0px 10px 0px 0px;

    }
    .one-room{
        margin-bottom: 10px;
        box-shadow: 1px 2px 3px #cccccc;
    }
</style>
