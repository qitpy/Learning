Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :bands do
        resources :members
      end
    end

    namespace :v2 do
      resources :bands
      resources :members
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
