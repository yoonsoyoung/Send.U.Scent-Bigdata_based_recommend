// 모달창(관심목록에 추가, 내가 가진 목록에 추가)
<template>
    <div id="ModalRoot">
        <div class="black-bg">
            <div class="modal-box p-3">
                <div class="modal-top">
                    <p class="modal-title">가지고 있는 목록에 추가하시겠습니까?</p>
                </div>
                <div class="modal-middle">
                    <p class="perfume-name">" {{this.name}} "</p>
                </div>
                <div class="modal-bottom">
                    <div class="button-group">
                        <button class="cancel-btn" @click="closeBtn">취소</button>
                        <button class="add-btn" @click="addBtn()">추가</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import http from '../utils/http-common.js'
import swal from 'sweetalert';
import { mapState } from 'vuex';
export default {
    props: [
        "id",
        "name",
        "perfume_id"
    ],
    created() {
        this.user_No = this.userInfo.id;
        this.prodInfo.perfume_id = this.id;
        this.prodInfo.perfume_name = this.name;
    },
    computed: {
        ...mapState(["userInfo"])
    },
    methods: {
        closeBtn() {
            this.$emit("flag", false);
            },
        addBtn() {
            const Form = {
                "user_id" : this.userInfo.id,
                "perfume_id" : this.perfume_id
            }
            console.log(this.prodInfo.perfume_name)
            http.post('/have/insert', Form)
                .then((res) => {
                    if(res.data.result === "success") {
                        swal(this.prodInfo.perfume_name + " 향수를 보유 향수에 추가했습니다.");
                        this.$router.go()
                    } else {
                        swal("데이터를 처리하는 중 문제가 발생했습니다.")
                    }
                })
            this.$emit("flag", false);
        },
        
    },
    mounted() {
        
    },
    data() {
        return {
            prodInfo : {
                perfume_id: Number,
                perfume_name: String,
            }
        }
    },
}
</script>

<style lang="scss" scoped>
@import "../styles/common.scss";
* {
  font-family: $kor-font-family;
}
#ModalRoot {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}
.black-bg {
  width: 100%;
  height: 100%;
  min-height: 1300px;
  position: relative;
  top: 0;
  left: 0;
  background-color: rgba(0,0,0,0.5);
  z-index: 10;
}
.modal-box {
  width: 370px;
  height: 260px;
  position: relative;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 20px 5px rgba(0, 0, 0, 0.25);
  z-index: 20;
  display: grid;
  align-content: space-evenly;
  justify-content: center;
  align-items: center;
  justify-items: center;
}
.modal-top {
  
}
.modal-top > .modal-title {
  font-size: $body-font-size;
  font-weight: 700;
}
.modal-middle {
  width: 100%;
}
.perfume-name {
    font-size: $bodytitle-font-size;
    font-weight: bold;
}
.modal-bottom {
  width: 90%;
}
.button-group {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-content: center;
  justify-content: center;
  align-items: center;
}
.cancel-btn {
	width: 40%;
	height: 35px;
	border: none;
	border-radius: 50px;
	background: $gray-color;
	margin-right: 25px;
}
.add-btn {
	width: 40%;
	height: 35px;
	border: none;
	border-radius: 50px;
	background: $point-color;
}
</style>