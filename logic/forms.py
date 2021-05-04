from django import forms

from logic.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

    # def save(self, commit=True):
    #     comment = super(CommentForm, self).save(commit=False)
    #     comment.text = self.cleaned_data["text"]
    #     comment.user = self.request.user
    #     comment.blog =

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #
    #     if email is not None and password:
    #         self.user_cache = authenticate(self.request, email=email, password=password)
    #         if self.user_cache is None:
    #             raise forms.ValidationError(
    #                 self.error_messages['invalid_login'],
    #                 code='invalid_login',
    #                 params={'username': self.username_field.verbose_name},
    #             )
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #
    #     return self.cleaned_data
