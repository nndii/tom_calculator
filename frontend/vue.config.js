module.exports = {
  devServer: {
      port: 8080,
      proxy: {
          "^/calculator": {
            target: `${process.env.BACKEND_URL}`,
            changeOrigin: true,
            secure: false,
            pathRewrite: {
                '^/calculator': '/calculator'
            },
          }
      }
  }
}