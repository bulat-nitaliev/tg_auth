<template>
    <div>
        <main class="form-signin">
               
                <h5 class="title">После нажатия кнопки вы перейдете в диалог с нашим ботом @tg_analytics_bot.

                                В диалоге с ботом нажмите кнопку Start</h5>
                

        </main>
        <a :href="URL_TG_BOT"  target="_blank" class="telegram-button">Перейти к боту</a>
        <my-dialog v-model:show="isVisible">{{text}}</my-dialog>
    </div>
    
    
</template>

<script>
import {mapState, mapActions, mapMutations } from 'vuex'
import config from '@/config'
export default {
    data:() => {
        return{
            username: '',
            password: '',
            URL_TG_BOT: config.url_tg
            
        }
    },
    computed: {
        ...mapState({
            isAuth: state=> state.isAuth,
            isVisible: state=> state.isVisible,
            text: state=> state.text,
        })
    },
    methods: { 
        
        login(){
            this.$store.dispatch('userLogin', 
            {
                username: this.username,
                password: this.password,
            }
            )
            .then((res)=>{
                this.$router.push('/')
            })
            .catch(err=>{
                this.isVisible = err
                this.isVisible = true
            })
        },

    }
    
}
</script>

<style scoped>
.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.title {
    color: rgba(12, 38, 85, 0.856)
}
.telegram-button { 
    display: inline-block; 
    padding: 10px 20px; 
    background-color: #0088cc; /* Цвет фона кнопки */ 
    color: white; /* Цвет текста */ 
    text-decoration: none; /* Убираем подчеркивание у ссылки */ 
    border-radius: 4px; /* Скругление углов */ 
    } 
.telegram-button:hover { 
    background-color: #006699; /* Изменение цвета при наведении курсора */ 
    } 
</style>