from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# -------------------
# User registration form
# -------------------
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# -------------------
# Post form (with tags)
# -------------------
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        label='Tags (comma-separated)',
        widget=forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Handle tags if using a Tag model
            tags_str = self.cleaned_data.get('tags', '')
            if tags_str:
                tag_names = [t.strip() for t in tags_str.split(',')]
                for name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=name)
                    instance.tags.add(tag)
        return instance

# -------------------
# Comment form
# -------------------
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'})
    )

    class Meta:
        model = Comment
        fields = ['content']
