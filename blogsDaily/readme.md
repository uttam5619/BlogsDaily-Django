
class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment =models.CharField(max_length=500)
    slug=models.SlugField(max_length=150, blank=True)
    commented_on = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment