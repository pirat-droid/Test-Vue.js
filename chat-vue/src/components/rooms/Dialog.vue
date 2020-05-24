<template>
    <mu-col span="8" xl="9">
        <AddUsers :room="id"></AddUsers>
        <mu-container class="dialog">
            <mu-row direction="column"
                    justify-content="start"
                    align-items="end"
                    v-for="dialog in dialogs"
                    :key="dialog.id">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-row>
                <mu-text-field v-model="form.textarea"
                               multi-line :rows="4"
                               full-width
                               placeholder="Enter text message">

                </mu-text-field>
                <!--                <button @click="sendMes">qwedwe</button>-->
                <mu-button @click="sendMes" color="success"  align-items="end" >Enter</mu-button>
            </mu-row>
        </mu-container>

    </mu-col>
</template>

<script>
    import AddUsers from './AddUsers'
    export default {
        name: "Dialog",
        components:{
            AddUsers
        },
        props: {
            id: ''
        },
        data(){
            return{
                dialogs: '',
                form: {
                    textarea: '',
                },
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.LoadDialog()
            setInterval(() => {
                this.LoadDialog()
            }, 5000)
        },
        methods:{
            LoadDialog(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "GET",
                    data:{
                        room: this.id
                    },
                    success:(response) => {
                        this.dialogs = response.data.data
                    }
                })
            },
            sendMes(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "POST",
                    data:{
                        room: this.id,
                        text: this.form.textarea
                    },
                    success:(response) => {
                        this.LoadDialog()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .dialog{
        border: 1px solid #000;
    }
</style>
