<template>
  <div>
    <div class="imgContent">
      <Vspacer></Vspacer>
      <div class="imagePreview">
        <img :src="uploadedImage" style="width:10%;" />
      </div>
      <input type="file" class="file_input" name="photo" @change="onFileChange"  accept="image/*" />
      <button @click='onUploadImage'>画像判定してください</button>
    </div>
    <img :src = 'LRUrl' width="10%" height="auto">
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://localhost:5000'
export default {
  data: () => ({
    LRUrl: '',
    uploadedImage: ''
  }),
  methods: {
    // 選択した画像を反映
    onFileChange (e) {
      let files = e.target.files || e.dataTransfer.files
      this.createImage(files[0])
    },
    // アップロードした画像を表示
    createImage (file) {
      let reader = new FileReader()
      reader.onload = (e) => {
        this.uploadedImage = e.target.result
      }
      reader.readAsDataURL(file)
    },
    // 画像をサーバーへアップロード
    onUploadImage () {
      var params = new FormData()
      params.append('image', this.uploadedImage)
      // Axiosを用いてFormData化したデータをFlaskへPostしています。
      axios.post(`${API_URL}/classification`, params).then(response => {
        console.log(response)
        const status = response.data.status
        if (status === 'error') {
          console.log('ERROR')
        } else {
          this.LRUrl = response.data.response_data
        }
      })
    }
  }
}
</script>
