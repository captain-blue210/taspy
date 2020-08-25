<template>
    <v-row justify="center">
        <v-dialog v-model="showDialog">
            <v-card>
                <v-card-title>
                    <span class="headline">タスク登録</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12">
                                <v-text-field v-model="task.name" label="タスク名" required></v-text-field>
                            </v-col>
                            <v-col cols="12">
                                <v-menu
                                    ref="menu"
                                    v-model="menu"
                                    :close-on-content-click="false"
                                    :return-value.sync="task.expirationDm"
                                    transition="scale-transition"
                                    offset-y
                                    min-width="290px"
                                >
                                    <template v-slot:activator="{ on, attrs }">
                                    <v-text-field
                                        v-model="task.expirationDm"
                                        label="期限日"
                                        readonly
                                        v-bind="attrs"
                                        v-on="on"
                                    ></v-text-field>
                                    </template>
                                    <v-date-picker
                                        v-model="task.expirationDm"
                                        locale="ja-jp"
                                        no-title
                                        scrollable
                                        :day-format="date => new Date(date).getDate()"
                                    >
                                    <v-spacer></v-spacer>
                                    <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                                    <v-btn text color="primary" @click="$refs.menu.save(task.expirationDm)">OK</v-btn>
                                    </v-date-picker>
                                </v-menu>
                            </v-col>
                            <v-col>
                                <v-select
                                    v-model="task.status"
                                    label="ステータス"
                                    :items="statusItems"
                                >
                                </v-select>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        block
                        color="primary"
                        @click="addTask"
                    >
                        登録
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog
            v-model="showAlert"
            max-width="500px"
        >
            <v-card>
                <v-card-title>
                    {{message}}
                </v-card-title>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<script>
import axios from '~/plugins/axios'

export default {
    data() {
        return {
            task: {
                name: null,
                expirationDm: new Date().toISOString().substr(0, 10),
                status: null,
            },
            menu: false,
            showDialog: false,
            showAlert: false,
            message: '',
            statusItems: ['OPEN','IN PROGRESS','CLOSED']
        }
    },
    methods: {
        addTask: function(){
            axios
                .post('/api/task/',{
                    name: this.task.name,
                    expirationDm: this.task.expirationDm,
                    status: this.task.status,
                })
                .then(res => {
                    this.showDialog = false
                    this.showAlert = true
                    this.message = 'タスクを登録しました。'
                    this.$router.push('/')
                })
        }
    }
}
</script>
